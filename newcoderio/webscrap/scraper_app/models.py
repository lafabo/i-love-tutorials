from sqlalchemy import *

import settings

def db_connect():
	"""
	Connects to db
	"""
	# todo make sqline works!
	return create_engine('sqlite:///{0}'.format(settings.DATABASE['database']))