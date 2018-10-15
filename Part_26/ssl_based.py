import cherrypy

# pip install cython, pyopenssl

class SSLDemo(object):
	@cherrypy.expose
	def index(self):
		return 'This is SSL protected!'

if __name__ == '__main__':
	cherrypy.config.update({
			'server.socket_port' : 443,
			'server.ssl_module' : 'pyopenssl',
			'server.ssl_certificate' : '.\\certificate.crt',
			'server.ssl_private_key' : '.\\private.key',

		})
	cherrypy.quickstart(SSLDemo(),'/')