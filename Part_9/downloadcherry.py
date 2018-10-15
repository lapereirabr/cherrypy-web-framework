import cherrypy
import os
from cherrypy.lib.static import serve_file

class FileViewer(object):
	@cherrypy.expose
	def index(self):
		index_page  = "<ul>"

		for item in os.listdir(os.path.abspath(os.sep.join([os.getcwd(),'downloads']))):
			index_page += "<li><a href='/downloads/{0}' target='_blank'>{0}</a></li>".format(item)


		index_page += '</ul>'

		return index_page

	@cherrypy.expose
	def downloads(self, filepath):
		return serve_file(filepath,'application/x-download','attachment')

if __name__ == '__main__':
	conf = {
		'/' : { 'tools.staticdir.root' : os.path.abspath(os.getcwd())},
		'/downloads' : {
			'tools.staticdir.on' : True,
			'tools.staticdir.dir' : '.\\downloads',
		}
	}
	cherrypy.quickstart(FileViewer(),'/',conf)