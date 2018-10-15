import cherrypy
from cherrypy._cpdispatch import Dispatcher

class ForcedLowerCase(Dispatcher):
	def __call__(self, path_info):
		return Dispatcher.__call__(self, path_info.lower())

class CustomDispatchDemo(object):
	@cherrypy.expose
	def casesensitive(self, random_stuff):
		return 'This is the stuff I got: {}'.format(random_stuff)

	@cherrypy.expose
	def sensitive(self):
		return 'This is sensitive!'


if __name__ == '__main__':
	conf = {
		'/' : { 'request.dispatch':ForcedLowerCase()}
	}
	cherrypy.quickstart(CustomDispatchDemo(),'/',conf)