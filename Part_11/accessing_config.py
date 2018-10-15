import cherrypy

class AccessConfig(object):
	@cherrypy.expose
	def index(self):
		return 'user: {}, password : {}'.format(cherrypy.request.app.config['my_api']['api_user'],cherrypy.request.app.config['my_api']['api_password'])

if __name__ == '__main__':
	cherrypy.quickstart(AccessConfig(),'/','app.conf')