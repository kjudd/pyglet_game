import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 7
GAME_HEIGHT = 7
GAME_OVER = False
#### Put class definitions here ####
class Rock(GameElement):
	IMAGE = "Rock"
	SOLID = True


class Character(GameElement):
	IMAGE = "Princess"
	SOLID = True
	def next_pos(self, direction):
		if direction == "up" and self.y > 0:
			return (self.x, self.y-1)
		elif direction == "down" and self.y < 6:
			return (self.x, self.y+1)
		elif direction == "left" and self.x > 0:
			return (self.x-1, self.y)
		elif direction == "right" and self.x < 6:
			return (self.x+1, self.y)
		else:
			return (self.x, self.y)

		

	def __init__(self):
		GameElement.__init__(self)
		self.inventory = []



class Gem(GameElement):
	IMAGE = "BlueGem"
	SOLID = False
	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" % (len(player.inventory)))

class Orange_Gem(GameElement):
	IMAGE = "OrangeGem"
	SOLID = False
	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" % (len(player.inventory)))



class Heart(GameElement):
	IMAGE = "Heart"
	SOLID = True
	

class Bubble(GameElement):
	IMAGE = "SpeechBubble"
	SOLID = False


class Quokka(GameElement):
	IMAGE = "Quokka"
	SOLID = True
	def interact(self, player):
		bubble = Bubble()
		GAME_BOARD.register(bubble)
		GAME_BOARD.set_el(5, 2, bubble)	
		GAME_BOARD.draw_msg("Find a key to turn Quokka into a handsome prince!")
	
		if len(player.inventory) == 3:
			GAME_BOARD.del_el(5,2)
			GAME_BOARD.del_el(4,4)
			prince = Prince()
			GAME_BOARD.register(prince)
			GAME_BOARD.set_el(4, 4, prince)
			GAME_BOARD.draw_msg("Congratulations! Quokka is now a prince!")
			heart_positions = [
			(2, 1),
			(3, 1),
			(4, 1),
			(5, 1),
			(6, 1),
			(6, 2),
			(6, 3),
			(6, 4),
			(6, 5),
			(6, 6),
			(5, 6),
			(4, 6),
			(3, 6),
			(2, 6),
			(2, 5),
			(2, 4),
			(2, 3),
			(2, 2),
			(3, 3),
			(3, 5),
			(5, 3),
			(5, 5),
			(4, 2),
			(3, 2),
			(5, 2),
			(0,0),
			(0,1),
			(0,2),
			(0,3),
			(0,4),
			(0,5),
			(0, 6),
			(1, 0),
			(1, 1),
			(1, 2),
			(1, 3),
			(1, 4),
			(1, 5),
			(1, 6),
			(2, 0),
			(3, 0),
			(4, 0),
			(5, 0),
			(6, 0)	
			]
			hearts = []
			for pos in heart_positions:
				heart1 = Heart()
				GAME_BOARD.register(heart1)
				GAME_BOARD.set_el(pos[0], pos[1], heart1)
				hearts.append(heart1)
			for heart in hearts:
				print heart

class Key(GameElement):
	IMAGE = "Key"
	SOLID = False
	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("You've got the key! Go to Quokka!")

class Prince(GameElement):
	IMAGE = "Boy"
	SOLID = True

class Chest(GameElement):
	IMAGE = "Chest"
	SOLID = True
	def interact(self, player):
		if len(player.inventory) == 2:
			key = Key()
			GAME_BOARD.register(key)
			GAME_BOARD.set_el(1, 4, key)
			GAME_BOARD.draw_msg("Congrats! Now grab a key and walk to quokka")	

		else:
			GAME_BOARD.draw_msg("Collect all items")

		
class EnemyBug(GameElement):
	IMAGE = "EnemyBug"
	SOLID = True
	def next_pos1(self, direction):
		if direction == "up" and self.y > 0:
			return (self.x, self.y-2)
		elif direction == "down" and self.y < 6:
			return (self.x, self.y+2)
		elif direction == "left" and self.x > 0:
			return (self.x-2, self.y)
		elif direction == "right" and self.x < 6:
			return (self.x+2, self.y)
		else:
			return (self.x, self.y)
			



####   End class definitions    ####

def initialize():
    """Put game initialization code here"""

    #Initialize and register rock1
    rock_positions = [
    		(2, 1),
    		(1, 2),
    		(3, 2),	
    		]
    rocks = []
    for pos in rock_positions:
    	rock = Rock()
    	GAME_BOARD.register(rock)
    	GAME_BOARD.set_el(pos[0], pos[1], rock)
    	rocks.append(rock)

    #rocks [-1].SOLID = False

    for rock in rocks:
    	print rock


    #initializing a Princess
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    #message from our sponsors
    GAME_BOARD.draw_msg("This game is wicked awesome!")

    #initialize gem
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

    orange_gem = Orange_Gem()
    GAME_BOARD.register(orange_gem)
    GAME_BOARD.set_el(3, 3, orange_gem)

    quokka = Quokka()
    GAME_BOARD.register(quokka)
    GAME_BOARD.set_el(4, 4, quokka)

    bubble = Bubble()
    GAME_BOARD.register(bubble)

    chest = Chest()
    GAME_BOARD.register(chest)
    GAME_BOARD.set_el(1, 4, chest)

    key = Key()
    GAME_BOARD.register(key)

    prince = Prince()
    GAME_BOARD.register(prince)

    heart = Heart()
    GAME_BOARD.register(heart)

    global BUG
    BUG = EnemyBug()
    GAME_BOARD.register(BUG)
    GAME_BOARD.set_el(6, 0, BUG)



#keyboard interaction
def keyboard_handler():
	global GAME_OVER
	if GAME_OVER:
		return

	direction = None

	if KEYBOARD[key.UP]:
		direction = "up"
		GAME_BOARD.del_el(5,2)
	if KEYBOARD[key.DOWN]:
		direction = "down"
		GAME_BOARD.del_el(5,2)
	if KEYBOARD[key.LEFT]:
		direction = "left"
		GAME_BOARD.del_el(5,2)
	if KEYBOARD[key.RIGHT]:
		direction = "right"
		GAME_BOARD.del_el(5,2)
	
	
	if direction:
		next_location = PLAYER.next_pos(direction)
		next_x = next_location[0]
		next_y = next_location[1]

		existing_el = GAME_BOARD.get_el(next_x, next_y)


		if existing_el:
			existing_el.interact(PLAYER)

		if existing_el is None or not existing_el.SOLID:
			GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
			GAME_BOARD.set_el(next_x, next_y, PLAYER)

	if direction:
		next_location = BUG.next_pos1(direction)
		next_x = next_location[0]
		next_y = next_location[1]
		
		existing_el = GAME_BOARD.get_el(next_x, next_y)
 		if existing_el == PLAYER:
 			GAME_BOARD.draw_msg("Game over! You suck!")
 			#generate positions for bugs	
			bug_positions = [(x, y) for x in xrange(GAME_WIDTH) for y in xrange(GAME_HEIGHT)]
			bugs = []
			for pos in bug_positions:
				bug1 = EnemyBug()
				GAME_BOARD.register(bug1)
				GAME_BOARD.set_el(pos[0], pos[1], bug1)
				bugs.append(bug1)
			for bug in bugs:
				print bug

			GAME_OVER = True

		if existing_el is None or not existing_el.SOLID:
			GAME_BOARD.del_el(BUG.x, BUG.y)
			GAME_BOARD.set_el(next_x, next_y, BUG)


