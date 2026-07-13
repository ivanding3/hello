import pygame
from sys import exit
import sprites 
import ui 
import collisions 
import map_stuff 
import vars 



clock = pygame.time.Clock()

pygame.display.init()


background = pygame.transform.scale(pygame.image.load('BG image.png'),(map_stuff.map_size))
box = pygame.transform.scale(pygame.image.load('Green.webp'),(200,200))
box_rect = pygame.Rect((1000,500),(200,200))

file_len = 0



pygame.event.set_blocked(pygame.MOUSEMOTION)




game_running = True
while game_running:
    
    
    keys_pressed = pygame.key.get_pressed()

    vars.dt = clock.tick()/1000
    print(f'fps = {1/vars.dt}')

    #print(player.vel,player.accel,dt)
    sprites.player.movement()
    collisions.collision(map_stuff.random_obj)
    collisions.collision(map_stuff.floor)
    map_stuff.camera.follow_player()
    #sprites.player.air_res()
    sprites.player.gravity()
    #camera



    #print(pygame.event.get())
    

   


    #print(random_obj.right,player.left)
    
    #inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ui.debug_button.pressed:
                sprites.player.pos = (pygame.mouse.get_pos()[0] - map_stuff.camera.x,
                                        pygame.mouse.get_pos()[1] - map_stuff.camera.y)
            if ui.map_mode_button.pressed:
                map_stuff.map_maker.initializing(event)
        if event.type == pygame.MOUSEBUTTONUP:
            if ui.map_mode_button.pressed:
                map_stuff.map_maker.finalizing(event)

    


#drawing
    map_stuff.camera.surface.blit(background,(0,0))
    map_stuff.camera.surface.blit(map_stuff.floor.surface,(map_stuff.floor.pos))

    map_stuff.camera.surface.blit(map_stuff.random_obj.surface,map_stuff.random_obj.pos)
    # inefficient
    with open('map_objs.txt','r') as f:
        f = f.readlines()
        if len(f)> file_len:
            map_stuff.map_objects.clear()
            file_len = 0
            for line in f:
                data = line.split('/')
                pos = tuple(map(int,data[0].replace('(','').replace(')','').split(',')))     
                size = tuple(map(int,data[1].replace('(','').replace(')','').split(',')))
                img = data[2]
                file_len += 1
                
                map_stuff.map_objects.append(sprites.sprite(pos,size,img))                                               
            
                                                          
                
            
                            #make a dict or something that i can loop through for collisions and drawing
                            #make a timer for everything so i can see what the fuck is taking so dam long
    for obj in map_stuff.map_objects:
        map_stuff.camera.surface.blit(obj.surface,obj.pos)
        collisions.collision(obj)
    map_stuff.camera.surface.blit(sprites.player.surface, (sprites.player.pos))
    if ui.map_mode_button.pressed:
        map_stuff.map_maker.map_mode()
    vars.screen.blit(map_stuff.camera.surface,(0,0),map_stuff.camera.display_part)
    ui.test_button.run_button()
    ui.debug_button.run_button()
    ui.map_mode_button.run_button()
    #pygame.draw.circle(screen,(00,00,00),(-camera.x+800,-camera.y+450),70)

    pygame.display.flip()    
