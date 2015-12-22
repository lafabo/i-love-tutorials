class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bd = Song(['Happy Bday to you', 'I better stop here'])
bulls_lyrics = ["They rally around the family","With pockets full of shells"]
bulls_parade = Song(bulls_lyrics)


happy_bd.sing_me_a_song()
bulls_parade.sing_me_a_song()