import cherrypy

#http://localhost:8080/
#http://localhost:8080/HelloWorld
#http://localhost:8080/helloworld

class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		return 'Hello World!'

	@cherrypy.expose
	def HelloWorld(self):
		return 'Another hello world!'

if __name__ == '__main__':
	cherrypy.quickstart(HelloWorld(),'/')
