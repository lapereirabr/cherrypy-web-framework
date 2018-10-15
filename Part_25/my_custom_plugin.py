import cherrypy
from cherrypy.process import plugins

class MyCustomPlugin(plugins.SimplePlugin):
	def __init__(self, bus, db_class):
		plugins.SimplePlugin.__init__(self, bus)
		self.db = db_class()

	def start(self):
		self.bus.log('Starting up the DB bus!')
		self.bus.subscribe("operation",self.operation)

	def stop(self):
		self.bus.log('Stopping the DB bus!')
		self.bus.unsubscribe('operation',self.operation)

	def operation(self,entity):
		self.db.save(entity)

DatabasePlugin(cherrypy.engine, SQLiteDB).subscribe()
		