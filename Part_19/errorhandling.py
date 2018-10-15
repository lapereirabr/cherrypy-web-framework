import cherrypy

class ErrorDemo(object):
	@cherrypy.expose
	def simple(self):
		raise cherrypy.HTTPError(401,'Unauthorized access!')

	@cherrypy.expose
	def file(self, path):
		with cherrypy.HTTPError.handle(FileNotFoundError, 404):
			file = open(path)

if __name__ == '__main__':
	cherrypy.quickstart(ErrorDemo(),'/')