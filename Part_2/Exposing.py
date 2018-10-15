import cherrypy

class Calculator(object):
	@cherrypy.expose
	def index(self):
		return 'Welcome to the Calculator WebApp!'

	@cherrypy.expose
	def sum(self, a, b):
		return ' a + b = {}'.format(float(a) + float(b))

	@cherrypy.expose
	def multiply(self, a, b):
		return ' a * b = {}'.format(float(a) * float(b))

	def divide(self, a, b):
		return ' a / b = {}'.format(float(a) / float(b))

	def subtract(self, a, b):
		return ' a - b = {}'.format(float(a) - float(b))

	divide.exposed = True
	subtract.exposed = True

if __name__ == '__main__':
	#cherrypy.quickstart(Calculator(),'/')
	cherrypy.quickstart(Calculator(),'/adifferentroot')