from ..abc import Service
from ..status import Status
from .webapp import WebApplication

###

class WebService(Service):

	def __init__(self, app):
		super().__init__(app)
		self.webapp = WebApplication(app)

		self.app.fix(self.fix())


	async def fix(self):
		self.webapp.start(self.app)
		self.app.fix(self.post_start())

	async def post_start(self):
		self.set_status(Status.RUNNING)
