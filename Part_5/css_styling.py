import cherrypy
import os

class Calculator(object):
	@cherrypy.expose
	def index(self):
		return open('index.html')

	@cherrypy.expose
	def result(self, a, b, manipulate):
		if manipulate == 'sum':
			result = int(a) + int(b)
		elif manipulate == 'multiply':
			result = int(a) * int(b)
		elif manipulate == 'divide':
			result = int(a) / int(b)
		return '{} {} {} = {}'.format(a,manipulate,b,result)

if __name__ == '__main__':
	conf = {
		'/' : { 'tools.staticdir.root':os.path.abspath(os.getcwd())},
		'/static' : {
			'tools.staticdir.on' : True,
			'tools.staticdir.dir' : '.\\public',
		}
	}
	cherrypy.quickstart(Calculator(),'/',conf)