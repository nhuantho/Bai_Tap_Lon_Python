import pygame
from pygame.locals import *

#base trúng ufo
def check_base_ufo(ufo, base_rect, ufo_width, ufo_height):

    ufo_rect = pygame.Rect(ufo.get('x_loc'), ufo.get('y_loc'), ufo_width, ufo_height)
    #có va chạm
    if base_rect.colliderect(ufo_rect):
        return True
    #không có va chạm
    return False