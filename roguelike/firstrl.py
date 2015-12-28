import libtcodpy as libtcod


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

LIMIT_FPS = 20

color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

class Tile:
	#a tile of the map and it's properties
	def __init__(self, blocked, block_sight = None):
		self.blocked = blocked

		#by default if tile is blocked it will block sight
		if block_sight is None: block_sight = blocked
		self.block_sight = block_sight

class Object:
	#this is a generic object: the player, monster, item, etc..
	#it's always represented by a character
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color

	def move(self, dx, dy):
		#move by a given amount
		if not map[self.x + dx][self.y + dy].blocked:
			self.x += dx
			self.y += dy

	def draw(self):
		#set the color and than draw the character at it's position
		libtcod.console_set_default_foreground(con, self.color)
		libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

	def clear(self):
		#erase the character
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)


def render_all():

	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			wall = map[x][y].block_sight
			if wall:
				libtcod.console_set_char_background(con, x, y,  color_dark_wall, libtcod.BKGND_SET)
			else:
				libtcod.console_set_char_background(con, x, y,  color_dark_ground, libtcod.BKGND_SET)

	#draw all objects in the list
	for object in objects:
		object.draw()

	#blit content from var con to root console
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

# map
def make_map():
	global map

	#fill map with 'unblocked' tiles
	map = [[ Tile(False) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

	#test
	map[30][22].blocked = True
	map[30][22].block_sight = True
	map[50][22].blocked = True
	map[50][22].block_sight = True

# movement
def handle_keys():
	global playerx, playery
	# fullscreen and enter
	key = libtcod.console_check_for_keypress()

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# alt+enter: toggle fullscreen
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
	elif key.vk == libtcod.KEY_ESCAPE:
		return True

	# movement
	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		player.move(0, -1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		player.move(0, 1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		player.move(-1, 0)
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		player.move(1, 0)


#####################################
# Initialisation and main game loop #
#####################################

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#player
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)

npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)

objects = [npc, player]

#generate map
make_map()

while not libtcod.console_is_window_closed():

	render_all()
	libtcod.console_flush()

	#erase all objects at their old locatoons before thay move
	for object in objects:
		object.clear()

	# handle_keys and exit game
	game_exit = handle_keys()
	if game_exit:
		break


