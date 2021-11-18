import pygame
import os
import sys

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bài tập lớn Python')
background_image = pygame.image.load('image/back_ground.jpg').convert()
start_image=pygame.image.load('image/start.png')
exit_image=pygame.image.load('image/exit.png')

class Button:
    def __init__(self, x, y, image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x, y)
        self.click=False
    def draw(self):
        acttion=False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.click=True
                acttion=True
        if pygame.mouse.get_pressed()[0]==0:
            self.click=False
        game_screen.blit(self.image, (self.rect.x, self.rect.y))
        return acttion

start_button=Button(100, 200, start_image)
exit_button=Button(340, 200, exit_image)
        
run=True
while run:
    game_screen.fill((202, 228, 241))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    game_screen.blit(background_image, [0, 0])
    
    if exit_button.draw()==True:
        pygame.quit()
        sys.exit() 
    if start_button.draw()==True: 
        pygame.quit()
        os.system('python A_Main.py')
        sys.exit()
    pygame.display.update()
pygame.quit()