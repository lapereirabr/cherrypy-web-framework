import logging
import logging.config
import cherrypy

LOG_CONF = {'formatters': {'standard': {'format': '%(asctime)s [%(levelname)s] %(name)s: '
                                       '%(message)s'},
                'void': {'format': ''}},
 'handlers': {'cherrypy_access': {'backupCount': 20,
                                  'class': 'logging.handlers.RotatingFileHandler',
                                  'encoding': 'utf8',
                                  'filename': 'access.log',
                                  'formatter': 'void',
                                  'level': 'INFO',
                                  'maxBytes': 10485760},
              'cherrypy_console': {'class': 'logging.StreamHandler',
                                   'formatter': 'void',
                                   'level': 'INFO',
                                   'stream': 'ext://sys.stdout'},
              'cherrypy_error': {'backupCount': 20,
                                 'class': 'logging.handlers.RotatingFileHandler',
                                 'encoding': 'utf8',
                                 'filename': 'errors.log',
                                 'formatter': 'void',
                                 'level': 'INFO',
                                 'maxBytes': 10485760},
              'default': {'class': 'logging.StreamHandler',
                          'formatter': 'standard',
                          'level': 'INFO',
                          'stream': 'ext://sys.stdout'}},
 'loggers': {'': {'handlers': ['default'], 'level': 'INFO'},
             'cherrypy.access': {'handlers': ['cherrypy_access'],
                                 'level': 'INFO',
                                 'propagate': False},
             'cherrypy.error': {'handlers': ['cherrypy_console',
                                             'cherrypy_error'],
                                'level': 'INFO',
                                'propagate': False},
             'db': {'handlers': ['default'],
                    'level': 'INFO',
                    'propagate': False}},
 'version': 1}

logger = logging.getLogger()
db_logger = logging.getLogger()

class LogDemoAdvanced(object):
	@cherrypy.expose
	def index(self):
		cherrypy.log('This was logged from cherrypy!')
		logger.warning('This was a warning from the logger!')
		db_logger.error('This was an error from the DB logger!')
		return 'OK'

if __name__ == '__main__':
	cherrypy.config.update({
			'log.screen' : False,
			'log.access_file': '',
			'log.error_file' : ''
		})
	cherrypy.engine.unsubscribe('graceful',cherrypy.log.reopen_files)
	logging.config.dictConfig(LOG_CONF)
	cherrypy.quickstart(LogDemoAdvanced())