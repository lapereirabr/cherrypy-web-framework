import cherrypy

def consume(stuff):
	cherrypy.log('The stuff: {} was marked for consumption!'.format(stuff))

class McDonalds(object):
	@cherrypy.expose
	def index(self, menu = 'Happy Meal'):
		cherrypy.engine.publish('consume',menu)
		return 'Started preparing the menu: {}'.format(menu)

# cherrypy.engine.subscribe('channel',function)
# cherrypy.engine.unsubscribe('channel',consume)
# cherrypy.engine.publish('channel',<what you want to publish>)

if __name__ == '__main__':
	cherrypy.engine.subscribe('consume',consume)
	cherrypy.tree.mount(McDonalds(),'/')
	cherrypy.engine.start()
	cherrypy.engine.block()