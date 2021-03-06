import os, sys, configparser, argparse

class ConfigParser(configparser.ConfigParser):


	defaults = {

		'general': {
			'verbose': False,
			'config_file': '',
			'include': '',
		},

	}


	def __init__(self):
		super().__init__()

		parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description="TurboCat.io is a high performance streaming tool for a capture, transformation, and load of data.\nTurboCat.io is an open-source product of TeskaLabs Ltd.\nSee more at https://github.com/TeskaLabs/TurboCat.io\n\n",
		)
		parser.add_argument('-c', '--config', help='Specify file path to configuration file')
		parser.add_argument('-v', '--verbose', action='store_true', help='Print more information (enable debug output)')

		args = parser.parse_args()
		if args.verbose:
			self.defaults['general']['verbose'] = True

		if args.config is not None:
			self.defaults['general']['config_file'] = args.config


	def add_defaults(self, dictionary):
		'''
		Add defaults to a current configuration
		'''

		for section, keys in dictionary.items():
			section = str(section)

			if section not in self._sections:
				try:
					self.add_section(section)
				except ValueError:
					if self._strict:
						raise

			for key, value in keys.items():

				key = self.optionxform(str(key))
				if key in self._sections[section]:
					continue # Value exists, no default needed

				if value is not None:
					value = str(value)

				self.set(section, key, value)


	def load(self):
		'''
		This method should be called only once, any subsequent call will lead to undefined behaviour
		'''
		config_fname = self.defaults['general']['config_file']
		if config_fname != '':
			if not os.path.isfile(config_fname):
				print("Config file '{}' not found".format(config_fname), file=sys.stderr)
				sys.exit(os.EX_CONFIG)

			self.read(config_fname)

		# Load included configuration files
		includes = self.get('general', 'include', fallback='')
		if includes != '':
			for include in includes.split(os.pathsep):
				self.read(include)

		self.add_defaults(self.defaults)


	def describe(self):
		result = dict()
		for section in self._sections:
			result[section] = self._sections[section]
		return self._sections
###

Config = ConfigParser()
