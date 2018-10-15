import cherrypy
from cherrypy.lib import auth_basic

def validate_pass(realm, user, password):
	if user == 'admin' and password == 'Start!123':
		return True
	else:
		return False

class SecureApp(object):
	@cherrypy.expose
	def index(self):
		return 'Successfull authorization!'

if __name__ == '__main__':
	conf = {
		'/'	: {
			'tools.auth_basic.on':True,
			'tools.auth_basic.realm':'localhost',
			'tools.auth_basic.checkpassword': validate_pass,
			'tools.auth_basic.accept_charset':'UTF-8',
		}
	}
	cherrypy.quickstart(SecureApp(),'/',conf)