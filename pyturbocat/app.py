import logging, asyncio, os

from .config import Config
from .abc import Singleton


class Application(object, metaclass=Singleton):

	def __init__(self):
		self.loop = asyncio.get_event_loop()
		self.config = Config

		logging.basicConfig(level=logging.INFO)

		Config.load()


	def run(self):
		self.loop.run_until_complete(self.loop.shutdown_asyncgens())
		self.loop.close()

		return os.EX_OK
