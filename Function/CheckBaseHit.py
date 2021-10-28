import pygame
from pygame.locals import *

#base trúng tên lửa
def check_base_hit(base_rect, missile_ufo_x, missile_ufo_y, missile_ufo_width, missile_ufo_height):

    missile_ufo_rect=pygame.Rect(missile_ufo_x, missile_ufo_y, missile_ufo_width, missile_ufo_height)
    #có va chạm
    if missile_ufo_rect.colliderect(base_rect):
        return True
    #không có va chạm
    return False