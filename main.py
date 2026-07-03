import pygame
from sys import exit
from player_stuff import *
from collider_objs import *
from ui import *
from physics import *

screen_width = 1600
screen_height = 900
resolution = (screen_width,screen_height)

clock = pygame.time.Clock()

pygame.display.init()
screen = pygame.display.set_mode((resolution),vsync=1)

background = pygame.transform.scale(pygame.image.load('Untitled.jpg'),(resolution))


box = pygame.transform.scale(pygame.image.load('Green.webp'),(200,200))
box_rect = pygame.Rect((1000,500),(200,200))



margin = 5







game_running = True
while game_running:
    
    dt = clock.tick(1000)/1000
    keys_pressed = pygame.key.get_pressed()
    
    #movement x
    if keys_pressed[pygame.K_w] == True: #and if vel < a vel and if on ground
        #player.y_vel = -500 
        player.y_accel = -500
    elif keys_pressed[pygame.K_s] == True: # increase max accel down
        player.y_accel = 500 
    else:
        player.y_accel = 0
    player.x_vel += player.x_accel*dt
    player.x += player.x_vel*dt

    #movement y
    if keys_pressed[pygame.K_a] == True: #
        player.x_accel = -500
    elif keys_pressed[pygame.K_d] == True:
        player.x_accel = 500     
    else:
        player.x_accel = 0
    player.y_vel += player.y_accel*dt
    player.y += player.y_vel*dt    

        
  






    collision(random_obj)
    collision(floor)
    #physics()


    



   


    #print(random_obj.rect.right,player.left)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.pos = pygame.mouse.get_pos()  
    
#update
    player.pos = (player.x,player.y)
    player.topleft = player.pos
#drawing
    screen.blit(background,(0,0))
    screen.blit(floor.img,(floor.rect))
    #screen.blit(box,box_rect.topleft)
    screen.blit(random_obj.img,random_obj.rect)
    test_button.run_button()


    screen.blit(player.img, (player.pos))    
    pygame.display.flip()    
