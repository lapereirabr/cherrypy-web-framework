import cherrypy
from time import sleep

class Streamer(object):
	@cherrypy.expose
	def index(self):
		cherrypy.response.headers['Content-Type'] = 'text/plain'
		def content():
			for i in range(100):
				yield str(i)
				sleep(1)

		return content()
	index._cp_config = { 'response.stream' : True }

if __name__ == '__main__':
	cherrypy.quickstart(Streamer(),'/')