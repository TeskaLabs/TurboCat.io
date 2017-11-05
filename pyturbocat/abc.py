import abc, logging
from .status import Status

###

L = logging.getLogger(__name__)

###

class Singleton(type):

	'''
	A singleton meta class.
	Inprired by https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

	Usage:

	class MyClass(BaseClass, metaclass=Singleton):
    	pass

	'''

	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

###

class Module(object):

	def __init__(self, app):
		self.app = app

	def describe(self):
		return {
			'module': str(self.__class__.__module__),
			'name': str(self.__class__.__name__)
		}

###

class Service(abc.ABC):

	def __init__(self, app, status = Status.CONFIG):
		self.app = app
		self.status = status

	def describe(self):
		return {
			'module': str(self.__class__.__module__),
			'name': str(self.__class__.__name__),
			'status': self.status.describe(),
		}

	def set_status(self, status):
		L.warn("Status change at {} from {} to {}".format(self, self.status, status))
		self.status = status
