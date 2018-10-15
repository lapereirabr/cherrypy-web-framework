from time import time
import cherrypy

class Timer(cherrypy.Tool):
	def __init__(self):
		cherrypy.Tool.__init__(self, 'before_handler', self.start_timing, priority = 95)

	def _setup(self):
		cherrypy.Tool._setup(self)
		cherrypy.request.hooks.attach('before_finalize', self.end_timing, priority = 5)

	def start_timing(self):
		cherrypy.request._time = time()

	def end_timing(self):
		duration = time() - cherrypy.request._time
		cherrypy.log('The request to the page handler: %.20f' % duration)

cherrypy.tools.timeit = Timer()

class TimerDemo(object):
	@cherrypy.expose
	@cherrypy.tools.timeit()
	def index(self):
		return 'THe timed request was processed!'

if __name__ == '__main__':
	cherrypy.quickstart(TimerDemo(),'/')