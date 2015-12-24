"""
Here is some text game from book

I'm trying to make it by myself, and at this moment i completely don't know how.
I didn't make this exercise. Just rewrite from the book. I still don't clearly understand how classes works.
"""
'''
* Map
	- next_scene
	- opening_scene
* Engine
	- play
* Scene
	- enter
	* Death
	* Central Corridor
	* Laser Weapon Armory
	* The Bridge
	* Escape Pod
'''
from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		print "The scene is not yet configured. Subclass it and implement enter()"
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

	quips = [
		'You died. That\'s bad',
		'Game Over. Not good at all'
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentrallCorridor(Scene):

	def enter(self):
		def enter(self):
			print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
			print "your entire crew. You are the last surviving member and your last"
			print "mission is to get the neutron destruct bomb from the Weapons Armory,"
			print "put it in the bridge, and blow the ship up after getting into an "
			print "escape pod."
			print "\n"
			print "You're running down the central corridor to the Weapons Armory when"
			print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
			print "flowing around his hate filled body. He's blocking the door to the"
			print "Armory and about to pull a weapon to blast you."

			action = raw_input("> ")

			if action == 'shoot':
				print "You missed. And Gothon eats you."
				return 'death'

			if action == 'dodge':
				print "You tried and failed. Now you are ded"
				return 'death'

			if action == 'tell a joke':
				print "Gothon falls at the floor and starts laugh. You are safe. At leas for now"
				return 'death'

			else:
				print "Does not compute"
				return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the Weapon Armory. You see a bomb in container. It has keypad. Try to guess the code XXX less than in 10 times"
		code = "%d%d%d" % (randint(1,3), randint(1,3), randint(1,3))
		guess = raw_input('[keypad]> ')
		guesses = 0

		while guess != code and guess < 10:
			print "Access denied"
			guesses += 1
			guess = raw_input('[keypad]> ')

		if guess == code:
			print "You guess the code and took the bomb, now you are moving to the bridge where you can place it"
			return 'the_bridge'
		else:
			print "The bomb has blown up"
			return 'death'



class TheBridge(Scene):

	def enter(self):
		print 'You came to the bridge with bomb'

		action = raw_input("> ")

		if action == 'set the bomb':
			print 'You placed the bomb and run to the chamber with escape pod'
			return 'escape_pod'
		elif action == 'throw the bomb':
			print "BOOM!"
			return 'death'
		else:
			print 'Does not compute'
			return 'the_bridge'


class EscapePod(Scene):

	def enter(self):
		print 'You get to the ship chamber with escape pods. Some of 5 pods looks broken, \
				but there is no time to diagnostic. Which one you take?'
		good_pod = randint(1, 5)
		guess = int(raw_input('[pod #]>'))

		if guess != good_pod:
			print "You jumped to the pod, press the button and... nothing hapening. You are in trap. At least until bomb boom up"
			return 'death'
		else:
			print "You jumped to the pod, press the button and... pod easily slides out into space heading the planet. Ship exploded with all Gothons and other stupid shit\n\nYou WIN!"
			return 'finished'

class Map(object):

	scenes = {
		'central_corridor': CentrallCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod' : EscapePod(),
		'death': Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		return self.start_scene

	def next_scene(self, scene_name):
		self.scene_name = scene_name
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
