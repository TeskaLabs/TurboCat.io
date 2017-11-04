import logging, asyncio, os

from .config import Config
from .abc import Singleton


class Application(object, metaclass=Singleton):

	def __init__(self):
		self.loop = asyncio.get_event_loop()
		self.config = Config
		self.modules = []

		logging.basicConfig(level=logging.INFO)

		Config.load()


	def initialize_module(self, module_class):
		module = module_class(self)
		self.modules.append(module)


	def run(self):
		self.loop.run_until_complete(self.loop.shutdown_asyncgens())
		self.loop.close()

		return os.EX_OK
