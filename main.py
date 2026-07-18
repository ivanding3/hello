import pygame
from sys import exit
import sprites 
import ui 
import collisions 
import map_stuff 
import vars 
import json
from pathlib import Path



#collisions rework
clock = pygame.time.Clock()
pygame.display.init()
background = pygame.transform.scale(pygame.image.load(Path.cwd()/'assets'/'BG image.png'),(map_stuff.map_size))
background = pygame.Surface.convert(background)
file_len = 0



pygame.event.set_blocked(pygame.MOUSEMOTION)

frame = 0
map_stuff.map_maker.load_map()
map_stuff.main_camera.curr_room.update_room_objs()


game_running = True
while game_running:
    frame +=1
    #print(frame)

    margin = (sum(map(abs,sprites.player.vel))//100)
    if margin>5:
        vars.margin = margin
    
    
    
    #print(f'fps = {1/vars.dt}')

    #print(player.vel,player.accel,dt)

    

    map_stuff.main_camera.follow_player()

    #camera

    

    vars.events = pygame.event.get()
    vars.keys_pressed = pygame.key.get_pressed()   
    #inputs
    for event in vars.events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if ui.debug_button.pressed:
                print(sprites.player.pos)
                sprites.player.pos = (pygame.mouse.get_pos()[0] - map_stuff.main_camera.x,
                                        pygame.mouse.get_pos()[1] - map_stuff.main_camera.y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                sprites.player.dash()
            if event.key == pygame.K_z:
                sprites.player.create_crumble(sprites.crumble)
            
     

    if vars.keys_pressed[pygame.K_c]:
        sprites.player.jump()


    if vars.keys_pressed[pygame.K_LEFT] and vars.keys_pressed[pygame.K_RIGHT]:
        sprites.player.input_directionx = 0
    else:
        if vars.keys_pressed[pygame.K_LEFT]:
            sprites.player.input_directionx = -1
            sprites.player.move_left()                
        elif vars.keys_pressed[pygame.K_RIGHT]:
            sprites.player.input_directionx = 1
            sprites.player.move_right()
        else:
            sprites.player.input_directionx = 0

    if vars.keys_pressed[pygame.K_UP] and vars.keys_pressed[pygame.K_DOWN]:
        sprites.player.input_directiony = 0   
    else:
        if vars.keys_pressed[pygame.K_UP]:
            sprites.player.input_directiony = -1
        elif vars.keys_pressed[pygame.K_DOWN]:
            sprites.player.input_directiony = 1
            if not vars.keys_pressed[pygame.K_c]:
                sprites.player.fast_fall()
        else:
            sprites.player.input_directiony = 0
                            

                    


#drawing
    map_stuff.main_camera.surface.blit(background,(0,0))

    #print(sprites.player.vel)

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
                                                               
                
    




    map_stuff.main_camera.surface.blit(sprites.player.surface, (sprites.player.pos))

    #map_mode_button
    if ui.map_mode_button.pressed:
        map_stuff.map_maker.map_mode()

        for i in range(map_stuff.map_size[0]//16):
            pygame.draw.line(map_stuff.main_camera.surface,(200,200,200),(i*16,0),(i*16,map_stuff.map_size[1]))
        for i in range(map_stuff.map_size[1]//16):
            pygame.draw.line(map_stuff.main_camera.surface,(200,200,200),(0,i*16),(map_stuff.map_size[0],i*16))

    #for collider_obj in map_stuff.map_objects:
    #    map_stuff.main_camera.surface.blit(collider_obj.surface,collider_obj.pos)
    #    collisions.collision(sprites.player,collider_obj)
    #map_stuff.main_camera.surface.blit(map_stuff.spike1.surface,map_stuff.spike1.pos)
    #map_stuff.spike1.update()
    #

    #crumble
    if sprites.crumble.collided_top:
        sprites.crumble.crumble()
    if not sprites.crumble.crumbled:
        collisions.collision(sprites.player,sprites.crumble)
        map_stuff.main_camera.surface.blit(sprites.crumble.surface,sprites.crumble.pos)

   


    for obj in map_stuff.main_camera.curr_room.objs:
        collisions.collision(sprites.player,obj)
        map_stuff.main_camera.surface.blit(obj.surface,obj.pos)

    for spike in map_stuff.main_camera.curr_room.spikes:
        map_stuff.main_camera.surface.blit(spike.surface,spike.pos)
        spike.update()

    for loader in map_stuff.main_camera.curr_room.loaders:
        map_stuff.main_camera.surface.blit(loader.surface,loader.pos)
        loader.check_overlap()

    collisions.check_colliding(sprites.player)
    vars.screen.blit(map_stuff.main_camera.surface,(0,0),map_stuff.main_camera.display_part)


    sprites.player.update_movement()


    #print(sprites.player.colliding_left,sprites.player.colliding_right,sprites.player.colliding_top,sprites.player.colliding_bottom,sprites.player.vel_direction)
    #print(sprites.player.pos,sprites.player.vel,sprites.player.accel)

    for button in ui.buttons:
        button.run_button()
    if ui.map_mode_button.pressed:
        ui.run_map_subbuttons()

    pygame.display.update(pygame.Rect((0,0),vars.resolution))    
    vars.dt = clock.tick(75)/1000
    #print(sprites.player.accel,sprites.player.vel,sprites.player.pos)
    
    