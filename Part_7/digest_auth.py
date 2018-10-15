import cherrypy
from cherrypy.lib import auth_digest

USERS = {
	'admin':'Start!123'
}

class SecureApp(object):
	@cherrypy.expose
	def index(self):
		return 'Successfull authentication!'


if __name__ == '__main__':
	conf = {
		'/' : {
			'tools.auth_digest.on' : True,
			'tools.auth_digest.realm' : 'localhost',
			'tools.auth_digest.get_ha1' : auth_digest.get_ha1_dict_plain(USERS),
			'tools.auth_digest.key' : 'a565c27146791cfb',
			'tools.auth_basic.accept_charset' : 'UTF-8',
		}

	}
	cherrypy.quickstart(SecureApp(),'/',conf)