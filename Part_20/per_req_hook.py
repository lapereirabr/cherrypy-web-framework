import cherrypy

class HookDemo(object):
	@cherrypy.tools.register('before_finalize')
	def remote_ip_info():
		cherrypy.log(cherrypy.request.remote.ip)


	@cherrypy.expose
	@cherrypy.tools.remote_ip_info()
	def index(self):
		return 'OK - remote ip captured!'

if __name__ == '__main__':
	cherrypy.quickstart(HookDemo(),'/')