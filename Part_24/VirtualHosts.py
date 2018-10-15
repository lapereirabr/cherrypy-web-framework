import cherrypy

class Root(object):
	def __init__(self):
		self.app1 = App1() 
		self.app2 = App2()

class App1(object):
	@cherrypy.expose
	def index(self):
		return 'Hello from webapp 1'

class App2(object):
	@cherrypy.expose
	def index(self):
		return 'Hello from webapp 2'


if __name__ == '__main__':
	virtualhosts = {
		'mycorp1.com:8080' : '/app1',
		'mycorp2.com:8080' : '/app2',
	}

	conf = { 'request.dispatch' : cherrypy.dispatch.VirtualHost(**virtualhosts)}
	cherrypy.quickstart(Root(),'/',{'/':conf})