import pygame
from pygame.locals import *

#Ufo trúng tên lửa
def check_ufo_hit(ufo, missile_rect, ufo_width, ufo_height):

    ufo_rect = pygame.Rect(ufo.get('x_loc'), ufo.get('y_loc'), ufo_width, ufo_height)
    
    if missile_rect.colliderect(ufo_rect):
        # nếu va chạm với ufo không có phòng thủ, ufo nổ
        if ufo.get('ray_time') == 0:
	        ufo_hit = 'direct hit'
	    # nếu va chạm với tia phòng thủ, tên lửa bị phá
        else:
            ufo_hit	=	'missile destroyed'	
    # tên lửa không bắn trúng
    else:
        ufo_hit = 'no hit'

    return ufo_hit