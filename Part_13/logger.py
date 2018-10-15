import cherrypy

class LogDemo(object):
	@cherrypy.expose
	def index(self):
		cherrypy.log('The index page was hit!')
		return 'OK'


if __name__ == '__main__':
	conf = {
		'/' : {
			'log.access_file' : '.\\access_logs.txt',
			'log.error_file' : '.\\error_logs.txt',
			'log.screen' : False

		}
	}
	cherrypy.quickstart(LogDemo(),'/',conf)