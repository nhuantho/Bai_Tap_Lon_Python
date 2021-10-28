from pygame.locals import *
import random

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCOREBOARD_MARGIN = 4


MISSILE_PLATFORM = 31
MISSILE_SPEED = 10
GAME_MISSILES = 20


UFO_UPPER_Y = 20
UFO_LOWER_Y = 240
UFO_HIT_TIME = 20
UFO_OFF_TIME = 60
UFO_SCORE = 50


RANDOM_VERTICAL_CHANGE = 20
RANDOM_HORIZONTAL_CHANGE = 100
UFO_DIRECTIONS = ['left', 'right', 'up', 'down']

# di chuyển ufo
def move_ufo(ufo, ufo_width):

    if ufo.get('hit') is False:
        if ufo.get('direction') == 'left':
	        ufo['x_loc'] -= ufo.get('speed')

        elif ufo.get('direction') == 'right':
	        ufo['x_loc'] += ufo.get('speed')
        elif ufo.get('direction') == 'up':
	        ufo['y_loc'] -= ufo.get('speed')
        elif ufo.get('direction') == 'down':
	        ufo['y_loc'] += ufo.get('speed')
	

        # Ufo chạm màn hình bên trái, đặt lại tọa độ x và đổi hướng
        if ufo.get('x_loc') < 0:
	        ufo['x_loc'] = 0	
	        ufo['direction']	= 'right'
		

        # Ufo chạm màn hình bên phải, đặt lại tọa độ x và đổi hướng
        elif ufo.get('x_loc') > SCREEN_WIDTH - ufo_width:
	        ufo['x_loc'] = SCREEN_WIDTH - ufo_width
	        ufo['direction'] = 'left'
	

        # ufo bay quá cao, đặt lại tọa độ y và đổi hướng 
        elif ufo.get('y_loc') < UFO_UPPER_Y:
	        ufo['y_loc'] = UFO_UPPER_Y
	        ufo['direction'] = 'down'
	

        # ufo bay quá thấp, đặt lại tọa độ y và đổi hướng
        elif ufo.get('y_loc') > UFO_LOWER_Y:
            ufo['y_loc'] =	UFO_LOWER_Y	
            ufo['direction'] =	'up'	
        # ufo được đổi hướng ngẫu nhiên
        else:
	        if ufo.get('direction') ==	'up' or ufo.get('direction') == 'down':
	            ufo_direction_chance =	random.randint(0, RANDOM_VERTICAL_CHANGE)
	        else:	
	            ufo_direction_chance =	random.randint(0, RANDOM_HORIZONTAL_CHANGE)
		
	        if ufo_direction_chance ==	1:
	            ufo['direction'] = random.choice(UFO_DIRECTIONS)