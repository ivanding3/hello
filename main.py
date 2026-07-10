import pygame
from sys import exit
from sprites import *
from collider_objs import *
from ui import *
from physics import *
from map import *

#time_init = time.time()
screen_width = 1600
screen_height = 900
resolution = (screen_width,screen_height)

clock = pygame.time.Clock()

pygame.display.init()
screen = pygame.display.set_mode((1800,1000),vsync=1)

background = pygame.transform.scale(pygame.image.load('BG image.png'),(map_size))


box = pygame.transform.scale(pygame.image.load('Green.webp'),(200,200))
box_rect = pygame.Rect((1000,500),(200,200))



margin = 5







game_running = True
while game_running:
    
    
    keys_pressed = pygame.key.get_pressed()

    dt = clock.tick(10000)/1000

    #print(player.vel,player.accel,dt)
    player.movement(dt)
    collision(random_obj)
    collision(floor)
    camera.follow_player()
    player.air_res(dt)
    player.gravity(dt)
    #camera

    



   


    #print(random_obj.right,player.left)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.pos = (pygame.mouse.get_pos()[0] - camera.x ,pygame.mouse.get_pos()[1] - camera.y)
            
    


#drawing
    camera.surface.blit(background,(0,0))
    camera.surface.blit(floor.surface,(floor.rect))

    camera.surface.blit(random_obj.surface,random_obj.rect)
    


    camera.surface.blit(player.surface, (player.pos))
    screen.blit(camera.surface,(0,0),camera.display_part)
    test_button.run_button()
    #pygame.draw.circle(screen,(00,00,00),(-camera.x+800,-camera.y+450),70)
  
    pygame.display.flip()    
