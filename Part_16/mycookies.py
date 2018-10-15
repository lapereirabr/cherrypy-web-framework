import cherrypy

class MyCookieApp(object):
	@cherrypy.expose
	def index(self):
		cookie = cherrypy.request.cookie
		response = "<h1>The amount of cookies: {}</h1><ul>".format(len(cookie))

		for c in cookie.keys():
			response += '<li>name: {}, value: {}</li>'.format(c, cookie[c].value)

		response += "</ul>"

		return response


	@cherrypy.expose
	def setcookie(self):
		cookie = cherrypy.response.cookie
		cookie['cookieName'] = 'MySurprise'
		cookie['cookieName']['path'] = '/'
		cookie['cookieName']['max-age'] = 3600
		cookie['cookieName']['version'] = 1
		return 'The surprise is ready for you!'

if __name__ == '__main__':
	cherrypy.quickstart(MyCookieApp(),'/')