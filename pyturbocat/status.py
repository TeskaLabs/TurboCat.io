from enum import Enum

###

class Status(Enum):
	CRITICAL = (50, 'purple')
	ERROR = (40, 'red')
	CONFIG = (30, 'orange')
	RUNNING = (20, 'green')
	DONE = (10, 'gray')


	def __init__(self, level, color):
		self.level =level
		self.color = color


	def describe(self):
		return {
			'name': str(self.name),
			'level': self.level,
			'color': self.color
		}
