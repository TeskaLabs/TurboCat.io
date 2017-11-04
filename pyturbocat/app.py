import logging, asyncio, os

from .config import Config
from .abc import Singleton


class Application(object, metaclass=Singleton):

	def __init__(self):
		self.loop = asyncio.get_event_loop()
		self.config = Config
		self.modules = []
		self.services = {}
		self.fixes = []

		logging.basicConfig(level=logging.INFO)
		Config.load()


	def run(self):

		# Fix all actors
		while len(self.fixes) > 0:
			fixes = self.fixes
			self.fixes = []
			done, pending = self.loop.run_until_complete(asyncio.wait(fixes))
			self.fixes.extend(pending)

		self.loop.run_forever()

		self.loop.run_until_complete(self.loop.shutdown_asyncgens())
		self.loop.close()

		return os.EX_OK


	def fix(self, future):
		self.fixes.append(future)


	# Modules

	def module_init(self, module_class):
		module = module_class(self)
		self.modules.append(module)


	# Services

	def service_init(self, service_code, service_class):
		service = service_class(self)
		self.services[service_code] = service
