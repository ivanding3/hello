import pygame
from sys import exit
import sprites 
import collider_objs 
import ui 
import physics 
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
    physics.collision(collider_objs.random_obj)
    physics.collision(collider_objs.floor)
    sprites.camera.follow_player()
    sprites.player.air_res()
    sprites.player.gravity()
    #camera

    



   


    #print(random_obj.right,player.left)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            sprites.player.pos = (pygame.mouse.get_pos()[0] - sprites.camera.x ,pygame.mouse.get_pos()[1] - sprites.camera.y)
            
    


#drawing
    sprites.camera.surface.blit(background,(0,0))
    sprites.camera.surface.blit(collider_objs.floor.surface,(collider_objs.floor.rect))

    sprites.camera.surface.blit(collider_objs.random_obj.surface,collider_objs.random_obj.rect)
    


    sprites.camera.surface.blit(sprites.player.surface, (sprites.player.pos))
    vars.screen.blit(sprites.camera.surface,(0,0),sprites.camera.display_part)
    ui.test_button.run_button()
    #pygame.draw.circle(screen,(00,00,00),(-camera.x+800,-camera.y+450),70)
  
    pygame.display.flip()    
