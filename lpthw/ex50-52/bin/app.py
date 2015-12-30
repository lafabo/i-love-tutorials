import web
from gweb import gmap

urls = ('/game', 'GameEngine', '/','Index')

app = web.application(urls, globals())

if web.config.get('_session') is None:
	store = web.session.DiskStore('session')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session


render = web.template.render('templates/', base='layout')

class Index:
	def GET(self):
		session.room = gmap.START
		web.seeother('/game')

class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room = session.room)
		else:
			return render.you_died()

	def POST(self):
		form = web.input(action=None)

		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother('/game')

if __name__ == '__main__':
	app.run()

