import sys

import os
import pygame
from pygame.locals import *
import random

from Function import CheckUfoHit, MoveUfo, UpdateHitUfo, UpdateRay, CheckBaseHit , CheckBaseUfo

# Xác định màu sắc
LIGHT_YELLOW = (255, 255, 204)

WHITE = (255, 255, 255)

# Xác định hằng số
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCOREBOARD_MARGIN = 4


MISSILE_PLATFORM = 31
MISSILE_SPEED = 20
GAME_MISSILES = 100


UFO_UPPER_Y = 20
UFO_LOWER_Y = 240
UFO_HIT_TIME = 20
UFO_OFF_TIME = 60
UFO_SCORE = 50


RANDOM_VERTICAL_CHANGE = 20
RANDOM_HORIZONTAL_CHANGE = 100
UFO_DIRECTIONS = ['left', 'right', 'up', 'down']


RANDOM_RAY = 200
RANDOM_RAY_TIME_MAX = 120

RANDOM_RAY_TIME_MIN = 30


BASE_SPEED = 10


# Cài đặt

os.environ['SDL_VIDEO_CENTERED'] = '1' 
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bài tập lớn Python')

pygame.key.set_repeat(10, 20)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Helvetica', 16)


# Load ảnh

background_image = pygame.image.load('Bach_ground.png').convert()
base_image = pygame.image.load('base.png').convert_alpha()
base_explpded_imade=pygame.image.load('base_explpded.png').convert_alpha()

missile_image = pygame.image.load('missile.png').convert_alpha()
missile_fired_image = pygame.image.load('missile_.png').convert_alpha()
missile_ufo_fired_image = pygame.image.load('missile_ufo.png').convert_alpha()


ufo_1_image = pygame.image.load('ufo_1.png').convert_alpha()
ufo_2_image = pygame.image.load('ufo_2.png').convert_alpha()
ufo_1_exploded_image = pygame.image.load('ufo_1_exploded.png').convert_alpha()
ufo_2_exploded_image = pygame.image.load('ufo_2_exploded.png').convert_alpha()
ufo_ray_image_1 = pygame.image.load('ufo_ray_1.png').convert_alpha()
ufo_ray_image_2 = pygame.image.load('ufo_ray_2.png').convert_alpha()


# Load âm thanh
spaceship_hit_sound = pygame.mixer.Sound('spaceship_hit.ogg')
launch_sound = pygame.mixer.Sound('launch.ogg')
ray_sound=pygame.mixer.Sound('ray.ogg')



def main():

    # biến khởi tạo
    base_x = 300
    base_y = 430
    base_width = base_image.get_rect().width
    base_height=base_image.get_rect().height


    ufo_width = ufo_1_image.get_rect().width
    ufo_height = ufo_1_image.get_rect().height


    ray_width = ufo_ray_image_1.get_rect().width
    missile_ufo_width=missile_ufo_fired_image.get_rect().width
    missile_ufo_height=missile_ufo_fired_image.get_rect().width

    # khởi tạo ufo 1
    ufo_1_x = SCREEN_WIDTH - ufo_width
    ufo_1_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y) 
    ufo_1 = {'x_loc': ufo_1_x, 'y_loc': ufo_1_y, 'direction': 'left', 'hit': False, 'hit_time': 0, 'off_time': 0,
            'ray_time': 0, 'speed': 5}  
    missile_ufo_1_x=0
    missile_ufo_1_y=0
            
    # khởi tạo ufo 2
    ufo_2_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
    ufo_2 = {'x_loc': 0, 'y_loc': ufo_2_y, 'direction': 'right', 'hit': False, 'hit_time': 0, 'off_time': 0,
        'ray_time': 0, 'speed': 3}
    missile_ufo_2_x=0
    missile_ufo_2_y=0

    # khởi tạo ufo 3
    ufo_3_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
    ufo_3 = {'x_loc': 0, 'y_loc': ufo_3_y, 'direction': 'right', 'hit': False, 'hit_time': 0, 'off_time': 0,
        'ray_time': 0, 'speed': 4}
    missile_ufo_3_x=0
    missile_ufo_3_y=0

    # khởi tạo ufo 4
    ufo_4_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
    ufo_4 = {'x_loc': 0, 'y_loc': ufo_4_y, 'direction': 'right', 'hit': False, 'hit_time': 0, 'off_time': 0,
        'ray_time': 0, 'speed': 6}
    missile_ufo_4_x=0
    missile_ufo_4_y=0

    # khởi tạo ufo 5
    ufo_5_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
    ufo_5 = {'x_loc': 0, 'y_loc': ufo_5_y, 'direction': 'right', 'hit': False, 'hit_time': 0, 'off_time': 0,
        'ray_time': 0, 'speed': 6}
    missile_ufo_5_x=0
    missile_ufo_5_y=0

    # khởi tạo ufo 6
    ufo_6_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
    ufo_6 = {'x_loc': 0, 'y_loc': ufo_6_y, 'direction': 'right', 'hit': False, 'hit_time': 0, 'off_time': 0,
        'ray_time': 0, 'speed': 6}
    missile_ufo_6_x=0
    missile_ufo_6_y=0

    # khởi tạo ufo 7
    ufo_7_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
    ufo_7 = {'x_loc': 0, 'y_loc': ufo_7_y, 'direction': 'right', 'hit': False, 'hit_time': 0, 'off_time': 0,
        'ray_time': 0, 'speed': 6}
    missile_ufo_7_x=0
    missile_ufo_7_y=0

    # khởi tạo ufo 8
    ufo_8_y = random.randint(UFO_UPPER_Y, UFO_LOWER_Y)
    ufo_8 = {'x_loc': 0, 'y_loc': ufo_8_y, 'direction': 'right', 'hit': False, 'hit_time': 0, 'off_time': 0,
        'ray_time': 0, 'speed': 6}
    missile_ufo_8_x=0
    missile_ufo_8_y=0
    
    missile_x = 0
    missile_y = 0
    missile_firing = False


    missile_width = missile_image.get_rect().width
    missile_height = missile_image.get_rect().height
    

    score = 0
    hi_score = 0
    missiles = GAME_MISSILES
    game_over = False


    # vòng lặp game
    run=True
    while run:
        for event in pygame.event.get():
            key_pressed = pygame.key.get_pressed()	
									
			# ấn nút sang trái để phi cơ sang trái	
            if key_pressed[pygame.K_LEFT]:	
                base_x -= BASE_SPEED	
                if base_x < 0:	
                    base_x = 0		
									
			# ấn nút sang phải để phi cơ sang phải	
            elif key_pressed[pygame.K_RIGHT]:	
                base_x += BASE_SPEED	
                if base_x > SCREEN_WIDTH - base_width:	
                    base_x = SCREEN_WIDTH - base_width	
            # ấn nút lên để phi cơ lên trên	
            elif key_pressed[pygame.K_UP]:	
                base_y -= BASE_SPEED	
                if base_y <0:	
                    base_y = 0
            # ấn nút xuống để phi cơ xuống dưới
            elif key_pressed[pygame.K_DOWN]:	
                base_y += BASE_SPEED	
                if base_y > SCREEN_HEIGHT - base_height:	
                    base_y = SCREEN_HEIGHT - base_height
            # nhấn nút cách để bắn tên lửa
            elif key_pressed[pygame.K_SPACE] and missile_firing is False and game_over is False:
                missile_firing = True
                missile_x = base_x + MISSILE_PLATFORM
                missile_y = base_y - missile_height
                missiles -= 1
                launch_sound.play()
                if missiles == 0:
                    game_over = True
                        
            # nhấn Return khi kết thúc trò chơi, bắt đầu trò chơi mới
            elif key_pressed[pygame.K_RETURN] and game_over is True:
                game_over = False
                score = 0
                missiles = GAME_MISSILES

                        
            # người dùng thoát	
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # cập nhật vị trí tên lửa
        if missile_firing is True:
	        missile_y -= MISSILE_SPEED
	        if missile_y < 0: missile_firing = False
        



        # vẽ nền
        game_screen.blit(background_image, [0, 0])


        # vẽ máy bay
        game_screen.blit(base_image, [base_x, base_y])

        # vẽ tên lửa
        if missile_firing is True:
	        game_screen.blit(missile_fired_image, [missile_x, missile_y])
        else:
            game_screen.blit(missile_image, [base_x + MISSILE_PLATFORM, base_y - missile_height])
        
        # vẽ UFOs

        # ufo 1, ufo 2
        # cập nhật vị trí ufo
        MoveUfo.move_ufo(ufo_1, ufo_width)
        MoveUfo.move_ufo(ufo_2, ufo_width)

        # cập nhật khiêng
        UpdateRay.update_ray(ufo_1)
        UpdateRay.update_ray(ufo_2)

        missile_rect = pygame.Rect(missile_x, missile_y, missile_width, missile_height)

        if ufo_1.get('hit') is False and missile_firing is True:
            ufo_hit	= CheckUfoHit.check_ufo_hit(ufo_1, missile_rect, ufo_width, ufo_height)	
            if	ufo_hit == 'missile	destroyed':	
                missile_firing = False
                pygame.mixer.stop()
				
            elif ufo_hit == 'direct hit':
                missile_firing = False
                score += UFO_SCORE * 2
                ufo_1['hit_time'] = UFO_HIT_TIME
                ufo_1['hit'] = True
				
                pygame.mixer.stop()
                spaceship_hit_sound.play()
        if ufo_2.get('hit') is False and missile_firing is True:
            ufo_hit = CheckUfoHit.check_ufo_hit(ufo_2, missile_rect, ufo_width, ufo_height)
            if ufo_hit == 'missile destroyed':
                missile_firing = False
                pygame.mixer.stop()

            elif ufo_hit == 'direct hit':
                missile_firing = False
                score += UFO_SCORE
                ufo_2['hit_time'] = UFO_HIT_TIME
                ufo_2['hit'] = True

                pygame.mixer.stop()
                spaceship_hit_sound.play()

        # cập nhật ufo bị tấn công
        UpdateHitUfo.update_hit_ufo(ufo_1, SCREEN_WIDTH - ufo_width, 'left')
        UpdateHitUfo.update_hit_ufo(ufo_2, 0, 'right')
        if ufo_1.get('hit_time') > 0:
	        game_screen.blit(ufo_1_exploded_image, [ufo_1.get('x_loc'), ufo_1.get('y_loc')])

        elif ufo_1.get('hit') is False:
	        game_screen.blit(ufo_1_image, [ufo_1.get('x_loc'), ufo_1.get('y_loc')])
	
        if ufo_2.get('hit_time') > 0:
	        game_screen.blit(ufo_2_exploded_image, [ufo_2.get('x_loc'), ufo_2.get('y_loc')])

        elif ufo_2.get('hit') is False:
	        game_screen.blit(ufo_2_image, [ufo_2.get('x_loc'), ufo_2.get('y_loc')])
	
        # vẽ khiêng
        if ufo_1.get('ray_time') > 0:
	        ray_x = ufo_1.get('x_loc') + (ufo_width - ray_width) / 2
	        ray_y = ufo_1.get('y_loc') + ufo_height
	        if ufo_1.get('ray_time') % 4 == 0 or ufo_1.get('ray_time') % 5 == 0:
	            game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
	        else:
	            game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])
	
        if ufo_2.get('ray_time') > 0:
	        ray_x = ufo_2.get('x_loc') + (ufo_width - ray_width) / 2
	        ray_y = ufo_2.get('y_loc') + ufo_height
	        if ufo_2.get('ray_time') % 4 == 0 or ufo_2.get('ray_time') % 5 == 0:
	            game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
	        else:
	            game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])
        
        #đạn ufo
        if ufo_1.get('ray_time') > 0:
	        missile_ufo_1_x = ufo_1.get('x_loc') + ufo_width
	        missile_ufo_1_y = ufo_1.get('y_loc') + ufo_height
        if(missile_ufo_1_x!=0 and missile_ufo_1_y!=0):   
            game_screen.blit(missile_ufo_fired_image, [missile_ufo_1_x, missile_ufo_1_y])
            missile_ufo_1_y+=10

        if ufo_2.get('ray_time') > 0:
	        missile_ufo_2_x = ufo_2.get('x_loc') + ufo_width
	        missile_ufo_2_y = ufo_2.get('y_loc') + ufo_height
        if(missile_ufo_2_x!=0 and missile_ufo_2_y!=0):   
            game_screen.blit(missile_ufo_fired_image, [missile_ufo_2_x, missile_ufo_2_y])
            missile_ufo_2_y+=15

        #level 2 thêm 1 ufo 3
        if int(score)>=200:
            # cập nhật vị trí ufo 
            MoveUfo.move_ufo(ufo_3, ufo_width)

            # cập nhật khiêng
            UpdateRay.update_ray(ufo_3)

            if ufo_3.get('hit') is False and missile_firing is True:
                ufo_hit = CheckUfoHit.check_ufo_hit(ufo_3, missile_rect, ufo_width, ufo_height)
                if ufo_hit == 'missile destroyed':
                    missile_firing = False
                    pygame.mixer.stop()

                elif ufo_hit == 'direct hit':
                    missile_firing = False
                    score += UFO_SCORE
                    ufo_3['hit_time'] = UFO_HIT_TIME
                    ufo_3['hit'] = True

                    pygame.mixer.stop()
                    spaceship_hit_sound.play()

            # cập nhật ufo bị tấn công
            UpdateHitUfo.update_hit_ufo(ufo_3, 0, 'right')

            if ufo_3.get('hit_time') > 0:
                game_screen.blit(ufo_2_exploded_image, [ufo_3.get('x_loc'), ufo_3.get('y_loc')])

            elif ufo_3.get('hit') is False:
                game_screen.blit(ufo_2_image, [ufo_3.get('x_loc'), ufo_3.get('y_loc')])
 
            if ufo_3.get('ray_time') > 0:
                ray_x = ufo_3.get('x_loc') + (ufo_width - ray_width) / 2
                ray_y = ufo_3.get('y_loc') + ufo_height
                if ufo_3.get('ray_time') % 4 == 0 or ufo_3.get('ray_time') % 5 == 0:
                    game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
                else:
                    game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])
            # đạn ufo 3
            if ufo_3.get('ray_time') > 0:
                missile_ufo_3_x = ufo_3.get('x_loc') + ufo_width
                missile_ufo_3_y = ufo_3.get('y_loc') + ufo_height
            if(missile_ufo_3_x!=0 and missile_ufo_3_y!=0):   
                game_screen.blit(missile_ufo_fired_image, [missile_ufo_3_x, missile_ufo_3_y])
                missile_ufo_3_y+=20
        
        # level 3 thêm 2 ufo 4, 5
        if int(score)>=500:
            #ufo 4
            # cập nhật vị trí ufo
            MoveUfo.move_ufo(ufo_4, ufo_width)
            # cập nhật khiêng
            UpdateRay.update_ray(ufo_4)

            if ufo_4.get('hit') is False and missile_firing is True:
                ufo_hit = CheckUfoHit.check_ufo_hit(ufo_4, missile_rect, ufo_width, ufo_height)
                if ufo_hit == 'missile destroyed':
                    missile_firing = False
                    pygame.mixer.stop()

                elif ufo_hit == 'direct hit':
                    missile_firing = False
                    score += UFO_SCORE
                    ufo_4['hit_time'] = UFO_HIT_TIME
                    ufo_4['hit'] = True

                    pygame.mixer.stop()
                    spaceship_hit_sound.play()
            # cập nhật ufo bị tấn công
            UpdateHitUfo.update_hit_ufo(ufo_4, 0, 'right')

            if ufo_4.get('hit_time') > 0:
                game_screen.blit(ufo_1_exploded_image, [ufo_4.get('x_loc'), ufo_4.get('y_loc')])

            elif ufo_4.get('hit') is False:
                game_screen.blit(ufo_1_image, [ufo_4.get('x_loc'), ufo_4.get('y_loc')])

            if ufo_4.get('ray_time') > 0:
                ray_x = ufo_4.get('x_loc') + (ufo_width - ray_width) / 2
                ray_y = ufo_4.get('y_loc') + ufo_height
                if ufo_4.get('ray_time') % 4 == 0 or ufo_4.get('ray_time') % 5 == 0:
                    game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
                else:
                    game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])

            # đạn ufo 
            if ufo_4.get('ray_time') > 0:
                missile_ufo_4_x = ufo_4.get('x_loc') + ufo_width
                missile_ufo_4_y = ufo_4.get('y_loc') + ufo_height
            if(missile_ufo_4_x!=0 and missile_ufo_4_y!=0):   
                game_screen.blit(missile_ufo_fired_image, [missile_ufo_4_x, missile_ufo_4_y])
                missile_ufo_4_y+=25

            #ufo 5
            # cập nhật vị trí ufo 
            MoveUfo.move_ufo(ufo_5, ufo_width)

            # cập nhật khiêng
            UpdateRay.update_ray(ufo_5)

            if ufo_5.get('hit') is False and missile_firing is True:
                ufo_hit = CheckUfoHit.check_ufo_hit(ufo_5, missile_rect, ufo_width, ufo_height)
                if ufo_hit == 'missile destroyed':
                    missile_firing = False
                    pygame.mixer.stop()

                elif ufo_hit == 'direct hit':
                    missile_firing = False
                    score += UFO_SCORE
                    ufo_5['hit_time'] = UFO_HIT_TIME
                    ufo_5['hit'] = True

                    pygame.mixer.stop()
                    spaceship_hit_sound.play() 
            
            # cập nhật ufo bị tấn công
            UpdateHitUfo.update_hit_ufo(ufo_5, 0, 'right')

            if ufo_5.get('hit_time') > 0:
                game_screen.blit(ufo_2_exploded_image, [ufo_5.get('x_loc'), ufo_5.get('y_loc')])

            elif ufo_5.get('hit') is False:
                game_screen.blit(ufo_2_image, [ufo_5.get('x_loc'), ufo_5.get('y_loc')])
 
            if ufo_5.get('ray_time') > 0:
                ray_x = ufo_5.get('x_loc') + (ufo_width - ray_width) / 2
                ray_y = ufo_5.get('y_loc') + ufo_height
                if ufo_5.get('ray_time') % 4 == 0 or ufo_5.get('ray_time') % 5 == 0:
                    game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
                else:
                    game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])
            # đạn ufo 
            if ufo_5.get('ray_time') > 0:
                missile_ufo_5_x = ufo_5.get('x_loc') + ufo_width
                missile_ufo_5_y = ufo_5.get('y_loc') + ufo_height
            if(missile_ufo_5_x!=0 and missile_ufo_5_y!=0):   
                game_screen.blit(missile_ufo_fired_image, [missile_ufo_5_x, missile_ufo_5_y])
                missile_ufo_5_y+=25
           
        # level 4 thêm 3 ufo 6, 7, 8
        if int(score)>=1000:
            #ufo 6
            # cập nhật vị trí ufo
            MoveUfo.move_ufo(ufo_6, ufo_width)
            # cập nhật khiêng
            UpdateRay.update_ray(ufo_6)

            if ufo_6.get('hit') is False and missile_firing is True:
                ufo_hit = CheckUfoHit.check_ufo_hit(ufo_6, missile_rect, ufo_width, ufo_height)
                if ufo_hit == 'missile destroyed':
                    missile_firing = False
                    pygame.mixer.stop()

                elif ufo_hit == 'direct hit':
                    missile_firing = False
                    score += UFO_SCORE
                    ufo_6['hit_time'] = UFO_HIT_TIME
                    ufo_6['hit'] = True

                    pygame.mixer.stop()
                    spaceship_hit_sound.play()
            # cập nhật ufo bị tấn công
            UpdateHitUfo.update_hit_ufo(ufo_6, 0, 'right')

            if ufo_6.get('hit_time') > 0:
                game_screen.blit(ufo_1_exploded_image, [ufo_6.get('x_loc'), ufo_6.get('y_loc')])

            elif ufo_6.get('hit') is False:
                game_screen.blit(ufo_1_image, [ufo_6.get('x_loc'), ufo_6.get('y_loc')])

            if ufo_6.get('ray_time') > 0:
                ray_x = ufo_6.get('x_loc') + (ufo_width - ray_width) / 2
                ray_y = ufo_6.get('y_loc') + ufo_height
                if ufo_6.get('ray_time') % 4 == 0 or ufo_6.get('ray_time') % 5 == 0:
                    game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
                else:
                    game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])

            # đạn ufo 
            if ufo_6.get('ray_time') > 0:
                missile_ufo_6_x = ufo_6.get('x_loc') + ufo_width
                missile_ufo_6_y = ufo_6.get('y_loc') + ufo_height
            if(missile_ufo_6_x!=0 and missile_ufo_6_y!=0):   
                game_screen.blit(missile_ufo_fired_image, [missile_ufo_6_x, missile_ufo_6_y])
                missile_ufo_6_y+=30

            #ufo 7
            # cập nhật vị trí ufo 
            MoveUfo.move_ufo(ufo_7, ufo_width)

            # cập nhật khiêng
            UpdateRay.update_ray(ufo_7)

            if ufo_7.get('hit') is False and missile_firing is True:
                ufo_hit = CheckUfoHit.check_ufo_hit(ufo_7, missile_rect, ufo_width, ufo_height)
                if ufo_hit == 'missile destroyed':
                    missile_firing = False
                    pygame.mixer.stop()

                elif ufo_hit == 'direct hit':
                    missile_firing = False
                    score += UFO_SCORE
                    ufo_7['hit_time'] = UFO_HIT_TIME
                    ufo_7['hit'] = True

                    pygame.mixer.stop()
                    spaceship_hit_sound.play() 
    
            # cập nhật ufo bị tấn công
            UpdateHitUfo.update_hit_ufo(ufo_7, 0, 'right')

            if ufo_7.get('hit_time') > 0:
                game_screen.blit(ufo_2_exploded_image, [ufo_7.get('x_loc'), ufo_7.get('y_loc')])

            elif ufo_7.get('hit') is False:
                game_screen.blit(ufo_2_image, [ufo_7.get('x_loc'), ufo_7.get('y_loc')])
 
            if ufo_7.get('ray_time') > 0:
                ray_x = ufo_7.get('x_loc') + (ufo_width - ray_width) / 2
                ray_y = ufo_7.get('y_loc') + ufo_height
                if ufo_7.get('ray_time') % 4 == 0 or ufo_7.get('ray_time') % 5 == 0:
                    game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
                else:
                    game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])
            # đạn ufo 
            if ufo_7.get('ray_time') > 0:
                missile_ufo_7_x = ufo_7.get('x_loc') + ufo_width
                missile_ufo_7_y = ufo_7.get('y_loc') + ufo_height
            if(missile_ufo_7_x!=0 and missile_ufo_7_y!=0):   
                game_screen.blit(missile_ufo_fired_image, [missile_ufo_7_x, missile_ufo_7_y])
                missile_ufo_7_y+=30
            #ufo 8
            # cập nhật vị trí ufo
            MoveUfo.move_ufo(ufo_8, ufo_width)
            # cập nhật khiêng
            UpdateRay.update_ray(ufo_8)

            if ufo_8.get('hit') is False and missile_firing is True:
                ufo_hit = CheckUfoHit.check_ufo_hit(ufo_8, missile_rect, ufo_width, ufo_height)
                if ufo_hit == 'missile destroyed':
                    missile_firing = False
                    pygame.mixer.stop()

                elif ufo_hit == 'direct hit':
                    missile_firing = False
                    score += UFO_SCORE
                    ufo_8['hit_time'] = UFO_HIT_TIME
                    ufo_8['hit'] = True

                    pygame.mixer.stop()
                    spaceship_hit_sound.play()
            # cập nhật ufo bị tấn công
            UpdateHitUfo.update_hit_ufo(ufo_8, 0, 'right')

            if ufo_8.get('hit_time') > 0:
                game_screen.blit(ufo_1_exploded_image, [ufo_8.get('x_loc'), ufo_8.get('y_loc')])

            elif ufo_8.get('hit') is False:
                game_screen.blit(ufo_1_image, [ufo_8.get('x_loc'), ufo_8.get('y_loc')])

            if ufo_8.get('ray_time') > 0:
                ray_x = ufo_8.get('x_loc') + (ufo_width - ray_width) / 2
                ray_y = ufo_8.get('y_loc') + ufo_height
                if ufo_8.get('ray_time') % 4 == 0 or ufo_8.get('ray_time') % 5 == 0:
                    game_screen.blit(ufo_ray_image_2, [ray_x, ray_y])
                else:
                    game_screen.blit(ufo_ray_image_1, [ray_x, ray_y])

            # đạn ufo 
            if ufo_8.get('ray_time') > 0:
                missile_ufo_8_x = ufo_8.get('x_loc') + ufo_width
                missile_ufo_8_y = ufo_8.get('y_loc') + ufo_height
            if(missile_ufo_8_x!=0 and missile_ufo_8_y!=0):   
                game_screen.blit(missile_ufo_fired_image, [missile_ufo_8_x, missile_ufo_8_y])
                missile_ufo_8_y+=30

        # trò chơi kết thúc
        base_rect=pygame.Rect(base_x, base_y, base_width, base_height)

        # máy bay chạm đạn
        if CheckBaseHit.check_base_hit(base_rect, missile_ufo_1_x, missile_ufo_1_y, missile_ufo_width, missile_ufo_height)==True:
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseHit.check_base_hit(base_rect, missile_ufo_2_x, missile_ufo_2_y, missile_ufo_width, missile_ufo_height)==True:
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseHit.check_base_hit(base_rect, missile_ufo_3_x, missile_ufo_3_y, missile_ufo_width, missile_ufo_height)==True:
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseHit.check_base_hit(base_rect, missile_ufo_4_x, missile_ufo_4_y, missile_ufo_width, missile_ufo_height)==True:
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseHit.check_base_hit(base_rect, missile_ufo_6_x, missile_ufo_6_y, missile_ufo_width, missile_ufo_height)==True:
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseHit.check_base_hit(base_rect, missile_ufo_7_x, missile_ufo_7_y, missile_ufo_width, missile_ufo_height)==True:
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseHit.check_base_hit(base_rect, missile_ufo_8_x, missile_ufo_8_y, missile_ufo_width, missile_ufo_height)==True:
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        # máy bay chạm ufo
        if CheckBaseUfo.check_base_ufo(ufo_1, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseUfo.check_base_ufo(ufo_2, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseUfo.check_base_ufo(ufo_3, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()

        if CheckBaseUfo.check_base_ufo(ufo_4, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()
        
        if CheckBaseUfo.check_base_ufo(ufo_5, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()
        
        if CheckBaseUfo.check_base_ufo(ufo_6, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()
        
        if CheckBaseUfo.check_base_ufo(ufo_7, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()
        
        if CheckBaseUfo.check_base_ufo(ufo_8, base_rect, ufo_width, ufo_height):
            game_over=True
            missile_firing=False
            game_screen.blit(base_explpded_imade, [base_x, base_y])
            pygame.mixer.stop()
            spaceship_hit_sound.play()
        
        if game_over is True and missile_firing is False:
	        if score > hi_score:
	            hi_score = score
	
	        display_game_over()
            
	

        # hiển thị bảng điểm
        score_text = 'Score: ' + str(score)
        display_scoreboard_data(score_text, 'left')
        missile_text = 'Missiles: ' + str(missiles)
        display_scoreboard_data(missile_text, 'centre')


        hi_score_text = 'Point best: ' + str(hi_score)
        display_scoreboard_data(hi_score_text, 'right')


        pygame.display.update()

        clock.tick(30)

# hiển thị dữ liệu bảng điểm
def display_scoreboard_data(scoreboard_text, alignment):

    display_text = font.render(scoreboard_text, True, LIGHT_YELLOW)
    text_rect = display_text.get_rect()
    
    text_loc = [0, 0]

    if alignment == 'left':
        text_loc = [SCOREBOARD_MARGIN, SCOREBOARD_MARGIN]

    elif alignment == 'right':
        text_loc = [SCREEN_WIDTH - text_rect.width - SCOREBOARD_MARGIN, SCOREBOARD_MARGIN]

    elif alignment == 'centre':
        text_loc = [(SCREEN_WIDTH - text_rect.width) / 2, SCOREBOARD_MARGIN]

    game_screen.blit(display_text, text_loc)

# hiển thị kết thúc trò chơi
def display_game_over():

    text_line_1 = font.render('GAME OVER', True, WHITE)
    text_rect_1 = text_line_1.get_rect()

    text_line_1_loc = [(SCREEN_WIDTH - text_rect_1.width) / 2, (SCREEN_HEIGHT / 2) - 16]

    text_line_2 = font.render('HIT RETURN FOR NEW GAME', True, WHITE)

    text_rect_2 = text_line_2.get_rect()
    text_line_2_loc = [(SCREEN_WIDTH - text_rect_2.width) / 2, (SCREEN_HEIGHT / 2) + 16]

    game_screen.blit(text_line_1, text_line_1_loc)
    game_screen.blit(text_line_2, text_line_2_loc)