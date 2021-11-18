from pygame.locals import *
import pygame
import random

RANDOM_RAY = 200
RANDOM_RAY_TIME_MAX = 120

RANDOM_RAY_TIME_MIN = 30


# cập nhật trạng thái khiêng
def update_ray(ufo):
    ray_sound=pygame.mixer.Sound('sound/ray.ogg')
    # Nếu chưa có một tia, thì cơ hội ngẫu nhiên sẽ có một tia
    if ufo.get('ray_time') == 0 and ufo.get('hit') is False:
        random_ray = random.randint(0, RANDOM_RAY)
        if random_ray == 1:
	        ufo['ray_time'] = random.randint(RANDOM_RAY_TIME_MIN, RANDOM_RAY_TIME_MAX)
        if random_ray==1:
            ray_sound.play()
	

    # Nếu có một tia, hãy giảm thời gian của nó
    elif ufo.get('ray_time') > 0:
        ufo['ray_time'] -= 1
        ray_sound.play()