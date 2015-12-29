import libtcodpy as libtcod


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

LIMIT_FPS = 20

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

MAX_ROOM_MONSTERS = 3

color_dark_wall = libtcod.Color(0, 0, 100)
color_light_wall = libtcod.Color(130, 110, 50)
color_dark_ground = libtcod.Color(50, 50, 150)
color_light_ground = libtcod.Color(200, 180, 50)

class Rect:
	# a rectangle on the map. (characterize a room)
	def __init__(self, x, y, w, h):
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h

	def center(self):
		center_x = (self.x1 + self.x2) / 2
		center_y = (self.y1 + self.y2) / 2
		return center_x, center_y

	def intersect(self, other):
		# returns true when rectangle intersects one another
		return (self.x1 <= other.x2 and self.x2 >= other.x1 and
				self.y1 <= other.y2 and self.y2 >= other.y1)


class Tile:
	# a tile of the map and it's properties
	def __init__(self, blocked, block_sight = None):
		self.blocked = blocked

		# fog of war
		self.explored = False

		#by default if tile is blocked it will block sight
		if block_sight is None: block_sight = blocked
		self.block_sight = block_sight

class Object:
	# this is a generic object: the player, monster, item, etc..
	# it's always represented by a character
	def __init__(self, x, y, char, name, color, blocks=False):
		self.name = name
		self.blocks = blocks
		self.x = x
		self.y = y
		self.char = char
		self.color = color

	def move(self, dx, dy):
		#move by a given amount
		if not is_blocked(self.x + dx, self.y + dy):
			self.x += dx
			self.y += dy

	def draw(self):
		#set the color and than draw the character at it's position
		if libtcod.map_is_in_fov(fov_map, self.x, self.y):
			libtcod.console_set_default_foreground(con, self.color)
			libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

	def clear(self):
		#erase the character
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)


def create_room(room):
	global map
	#go through the tiles and make passable
	for x in range(room.x1 + 1, room.x2):
		for y in range(room.y1 + 1, room.y2):
			map[x][y].blocked = False
			map[x][y].block_sight = False

def render_all():
	global color_dark_wall, color_light_wall
	global color_dark_ground, color_light_ground
	global fov_recompute

	if fov_recompute:
		#if player moved and etc
		fov_recompute = False
		libtcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)

		for y in range(MAP_HEIGHT):
			for x in range(MAP_WIDTH):
				wall = map[x][y].block_sight
				visible = libtcod.map_is_in_fov(fov_map, x, y)
				if not visible:
					if map[x][y].explored:
						if wall:
							libtcod.console_set_char_background(con, x, y,  color_dark_wall, libtcod.BKGND_SET)
						else:
							libtcod.console_set_char_background(con, x, y,  color_dark_ground, libtcod.BKGND_SET)
				else:
					#if visible
					if wall:
						libtcod.console_set_char_background(con, x, y, color_light_wall, libtcod.BKGND_SET)
					else:
						libtcod.console_set_char_background(con, x, y, color_light_ground, libtcod.BKGND_SET)
					map[x][y].explored = True


	#draw all objects in the list
	for object in objects:
		object.draw()



	#blit content from var con to root console
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

# map
def make_map():
	global map

	#fill map with 'unblocked' tiles
	map = [[ Tile(True)
		for y in range(MAP_HEIGHT)]
			for x in range(MAP_WIDTH)]

	rooms = []
	num_rooms =0

	for r in range(MAX_ROOMS):
		#random height and width
		w = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		h = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		#random position
		x = libtcod.random_get_int(0, 0, MAP_WIDTH - w - 1)
		y = libtcod.random_get_int(0, 0, MAP_HEIGHT - h - 1)

		new_room = Rect(x, y, w, h)
		failed = False
		for other_room in rooms:
			if new_room.intersect(other_room):
				failed = True
				break

		if not failed:
			# if no intersections paint new map tiles
			create_room(new_room)

			#add some content to this room
			place_objects(new_room)


			(new_x, new_y) = new_room.center()

			'''room_no = Object(new_x, new_y, chr(65+num_rooms), libtcod.white)
			objects.insert(0, room_no)'''

			if num_rooms == 0:
				player.x = new_x
				player.y = new_y

			else:
				#all rooms after the first:
				# connect it to the previous with tunnel

				# center coordinates of previous room
				(prev_x, prev_y) = rooms[num_rooms-1].center()

				if libtcod.random_get_int(0, 0, 1) == 1:
					create_h_tunnel(prev_x, new_x, prev_y)
					create_v_tunnel(prev_y, new_y, new_x)
				else:
					create_v_tunnel(prev_y, new_y, prev_x)
					create_h_tunnel(prev_x, new_x, new_y)

			rooms.append(new_room)
			num_rooms += 1


def create_h_tunnel(x1, x2, y):
	global map
	for x in range(min(x1, x2), max(x1, x2)+1):
		map[x][y].blocked = False
		map[x][y].block_sight = False

def create_v_tunnel(y1, y2, x):
	global map
	for y in range(min(y1, y2), max(y1, y2)+1):
		map[x][y].blocked = False
		map[x][y].block_sight = False

# movement
def handle_keys():
	global playerx, playery
	global fov_recompute
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
		fov_recompute = True
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		player.move(0, 1)
		fov_recompute = True
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		player.move(-1, 0)
		fov_recompute = True
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		player.move(1, 0)
		fov_recompute = True

def place_objects(room):
	# random number of monsters
	num_monsters = libtcod.random_get_int(0, 0, MAX_ROOM_MONSTERS)

	for i in range(num_monsters):
		# random spot for monsters
		x = libtcod.random_get_int(0, room.x1, room.x2)
		y = libtcod.random_get_int(0, room.y1, room.y2)

		if not is_blocked(x, y):
			if libtcod.random_get_int(0, 0, 100) < 80: # 80% chance to get the ork
				moster = Object(x, y, 'o', libtcod.desaturated_green, blocks=True)
			else:
				moster = Object(x, y, 'T', libtcod.darker_green, blocks=True)

		objects.append(moster)

def is_blocked(x, y):
	if map[x][y].blocked:
		return True

	for object in objects:
		if object.blocks and object.x == x and object.y == y:
			return True

	return False

#####################################
# Initialisation and main game loop #
#####################################

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#player
player = Object(0, 0, '@', 'player', libtcod.white, blocks=True)
objects = [player]

#generate map
make_map()

# lighting (FOV map)
fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
fov_recompute = True

for y in range(MAP_HEIGHT):
	for x in range(MAP_WIDTH):
		libtcod.map_set_properties(fov_map, x, y, not map[x][y].block_sight, not map[x][y].blocked)

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




