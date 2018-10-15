import cherrypy

class SessionDemo(object):
	@cherrypy.expose
	def index(self):
		if 'sessioncounter' not in cherrypy.session:
			cherrypy.session['sessioncounter'] = 0
		else:
			cherrypy.session['sessioncounter'] += 1

		return 'Number of sessions : {}'.format(cherrypy.session['sessioncounter'])

if __name__ == '__main__':
	conf = {
		'/' : {
			'tools.sessions.on' : True,
			'tools.sessions.storage_class' : cherrypy.lib.sessions.FileSession,
			'tools.sessions.storage_path' : '.\\session_store'
		}
	}
	cherrypy.quickstart(SessionDemo(),'/',conf)