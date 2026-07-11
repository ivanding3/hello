import pygame
from sys import exit
import sprites 
import ui 
import collisions 
import map 
import vars 



clock = pygame.time.Clock()

pygame.display.init()


background = pygame.transform.scale(pygame.image.load('BG image.png'),(map.map_size))


box = pygame.transform.scale(pygame.image.load('Green.webp'),(200,200))
box_rect = pygame.Rect((1000,500),(200,200))











game_running = True
while game_running:
    
    
    keys_pressed = pygame.key.get_pressed()

    vars.dt = clock.tick(240)/1000

    #print(player.vel,player.accel,dt)
    sprites.player.movement()
    collisions.collision(map.random_obj)
    collisions.collision(map.floor)
    map.camera.follow_player()
    sprites.player.air_res()
    sprites.player.gravity()
    #camera


    



   


    #print(random_obj.right,player.left)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            sprites.player.pos = (pygame.mouse.get_pos()[0] - map.camera.x ,pygame.mouse.get_pos()[1] - map.camera.y)
            
    


#drawing
    map.camera.surface.blit(background,(0,0))
    map.camera.surface.blit(map.floor.surface,(map.floor.rect))

    map.camera.surface.blit(map.random_obj.surface,map.random_obj.rect)
    


    map.camera.surface.blit(sprites.player.surface, (sprites.player.pos))
    vars.screen.blit(map.camera.surface,(0,0),map.camera.display_part)
    ui.test_button.run_button()
    #pygame.draw.circle(screen,(00,00,00),(-camera.x+800,-camera.y+450),70)
  
    pygame.display.flip()    
