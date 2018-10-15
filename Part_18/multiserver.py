import cherrypy
from cherrypy._cpserver import Server

class Hello(object):
	@cherrypy.expose
	def index(self):
		return 'OK'

if __name__ == '__main__':
	port = 8081
	for i in range(10):
		port += 1
		server = Server()
		server.socket_port = port
		server.subscribe()

	cherrypy.quickstart(Hello(),'/')
