import logging
from .service import WebService
from pyturbocat import Module

###

L = logging.getLogger(__name__)

###

class Module(Module):


	def __init__(self, app):
		super().__init__(app)
		app.service_init('web', WebService)
