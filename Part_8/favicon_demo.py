import cherrypy

class FaviconDemo(object):
	@cherrypy.expose
	def index(self):
		return 'This is the favicon demo!'

if __name__ == '__main__':
	conf = {
		'/favicon.ico' : {
			'tools.staticfile.on' : True,
			'tools.staticfile.filename' : r'C:\Users\Cyber\Desktop\CherryCourse\Part_8\favicon.ico',
		}
	}
	cherrypy.quickstart(FaviconDemo(),'/', conf)