from pygame.locals import *
import random

UFO_UPPER_Y = 20
UFO_LOWER_Y = 240
UFO_HIT_TIME = 20
UFO_OFF_TIME = 60
UFO_SCORE = 50

# cập nhật trạng thái của ufo khi bị bắn trúng
def update_hit_ufo(ufo, new_x_loc, new_direction):
    # UFO đã bị bắn trúng, hãy tính lại thời gian bị bắn
    if ufo.get('hit_time') > 0:
        ufo['hit_time'] -= 1

        # Khi thời gian tấn công bằng 0, UFO sẽ tắt màn hình
        if ufo.get('hit_time') == 0:
	        ufo['off_time'] = UFO_OFF_TIME
	

    # UFO đang tắt màn hình, giảm thời gian tắt màn hình
    elif ufo.get('off_time') > 0:
        ufo['off_time'] -= 1
        # Khi thời gian tắt màn hình đạt đến 0, hãy đặt vị trí và hướng UFO mới
        if ufo.get('off_time') == 0:
	        ufo['y_loc']	= random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
	        ufo['x_loc']	= new_x_loc
	        ufo['direction'] = new_direction
	        ufo['hit'] =	False