import abc

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
		pass

###

class Service(abc.ABC):


	def __init__(self, app):
		pass

