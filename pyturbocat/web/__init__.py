import logging
from pyturbocat import Module

###

L = logging.getLogger(__name__)

###

class Module(Module):


	def __init__(self, app):
		super().__init__(app)
