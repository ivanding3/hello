import pygame
from sys import exit
import sprites 
import ui 
import collisions 
import map_stuff 
import vars 
from pathlib import Path

vars.load_time = 1


file_len = 0
time = 0

#collisions rework
clock = pygame.time.Clock()
pygame.display.init()



pygame.event.set_blocked(pygame.MOUSEMOTION)



map_stuff.map_maker.load_map()
for key in map_stuff.map_objs:
    for loader in map_stuff.map_objs[key]['loaders']:
        loader.init_loaders()
map_stuff.main_camera.curr_room.update_room_objs()



while vars.game_running:


    if not map_stuff.main_camera.curr_room.pos ==  (2, 0):
        time += vars.dt

    if vars.menu_open:
        bad_name = sprites.player.vel,sprites.player.accel
        sprites.player.vel,sprites.player.accel = (0,0),(0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vars.game_running = False
            if event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE:
                vars.menu_open = False
                vars.load_time = 0.2
                sprites.player.vel,sprites.player.accel = bad_name
        ui.resume_b.run_button()
        if ui.resume_b.pressed:
            vars.menu_open = False
            vars.load_time = 0.2
            sprites.player.vel,sprites.player.accel = bad_name
        #ui.settings_b.run_button()
        #ui.controls_b.run_button()
        ui.quit_b.run_button()
        if ui.quit_b.pressed:
            vars.game_running = False
        pygame.display.flip()
    else:
        if sprites.player.utils > 0:
            sprites.player.surface = pygame.transform.scale(pygame.image.load(Path.cwd()/'assets'/'boxwithbox.png'),(64,64))
        else:
            sprites.player.surface = pygame.transform.scale(pygame.image.load(Path.cwd()/'assets'/'boxplayer.png'),(64,64))

        map_stuff.main_camera.follow_player()
        map_stuff.main_camera.stay_in_room()
        
        vars.events = pygame.event.get()
        vars.keys_pressed = pygame.key.get_pressed()  

        #inputs
        for event in vars.events:
            if event.type == pygame.QUIT:
                map_stuff.map_objs_to_json()
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                if ui.debug_button.pressed:
                    sprites.player.gravity_enabled = False
                    sprites.player.pos = (pygame.mouse.get_pos()[0] - map_stuff.main_camera.x,
                                            pygame.mouse.get_pos()[1] - map_stuff.main_camera.y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    #sprites.player.dash()
                    pass
                if event.key == pygame.K_z:
                    sprites.player.create_crumble(sprites.crumble)

                if event.key == pygame.K_ESCAPE:
                    vars.menu_open = True


        if ui.debug_button.pressed:
            sprites.player.gravity_enabled = False     
            sprites.player.utils = 10

        else:sprites.player.gravity_enabled = True

        if vars.keys_pressed[pygame.K_c]:
            sprites.player.jump()
        if vars.keys_pressed[pygame.K_LEFT] and vars.keys_pressed[pygame.K_RIGHT]:
            sprites.player.input_directionx = 0
        else:
            if vars.keys_pressed[pygame.K_LEFT]:
                sprites.player.input_directionx = -1
                sprites.player.move_left()        
                sprites.player.facing = -1        
            elif vars.keys_pressed[pygame.K_RIGHT]:
                sprites.player.input_directionx = 1
                sprites.player.move_right()
                sprites.player.facing = 1
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
        map_stuff.main_camera.surface.blit(map_stuff.main_camera.background,(0,0))
        map_stuff.main_camera.surface.blit(sprites.player.surface, (sprites.player.pos))

        #map_mode_button
        if ui.map_mode_button.pressed:
            map_stuff.map_maker.map_mode()
            for event in vars.events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    map_stuff.map_maker.del_obj()
            for i in range(map_stuff.map_size[0]//16):
                pygame.draw.line(map_stuff.main_camera.surface,(200,200,200),(i*16,0),(i*16,map_stuff.map_size[1]))
            for i in range(map_stuff.map_size[1]//16):
                pygame.draw.line(map_stuff.main_camera.surface,(200,200,200),(0,i*16),(map_stuff.map_size[0],i*16))



        #crumble


    


        for obj in map_stuff.main_camera.curr_room.objs:
            collisions.collision(sprites.player,obj)
            if collisions.overlapping(sprites.player,obj):
                sprites.player.overlapping = True
            else:
                sprites.player.overlapping = False
            map_stuff.main_camera.surface.blit(obj.surface,obj.pos)

        for spike in map_stuff.main_camera.curr_room.spikes:
            map_stuff.main_camera.surface.blit(spike.surface,spike.pos)
            spike.update()

        for loader in map_stuff.main_camera.curr_room.loaders:
            map_stuff.main_camera.surface.blit(loader.surface,loader.pos)
            loader.check_overlap()

        if sprites.crumble.collided_top:
            sprites.crumble.crumble()
        if not sprites.crumble.crumbled:
            collisions.collision(sprites.player,sprites.crumble)
            map_stuff.main_camera.surface.blit(sprites.crumble.surface,sprites.crumble.pos)
        collisions.check_colliding(sprites.player)

        if map_stuff.main_camera.curr_room.pos ==  (0, 0):
            text_surface = pygame.font.SysFont("geistpixelregular",30).render('Arrow keys to move, c to jump', True, (0,0,0))
            map_stuff.main_camera.surface.blit(text_surface,(200,400))
        if map_stuff.main_camera.curr_room.pos ==  (1, 0):
            text_surface = pygame.font.SysFont("geistpixelregular",30).render('Z to place box in the direction of arrow key input (diagonals exist)', True, (0,0,0))
            map_stuff.main_camera.surface.blit(text_surface,(400,150))
        if map_stuff.main_camera.curr_room.pos ==  (3, -1):
            text_surface = pygame.font.SysFont("geistpixelregular",60).render('Thanks for playing!', True, (0,0,0))
            map_stuff.main_camera.surface.blit(text_surface,(800,300))

        vars.screen.blit(map_stuff.main_camera.surface,(0,0),map_stuff.main_camera.display_part)



        sprites.player.check_pause()
        if not sprites.player.paused:
            
            sprites.player.update_movement()


        
            

        ui.draw_text(f'time = {round(time,3)}',30,(99,99,99),(0,0),vars.screen)
        ui.draw_text(f'deaths = {sprites.player.death_count}',30,(99,99,99),(vars.screen_width-200,0),vars.screen)

        #for button in ui.buttons:
        #   button.run_button()
        #if ui.map_mode_button.pressed:
        #    ui.run_map_subbuttons()

        if not sprites.player.paused:
            pygame.display.update(pygame.Rect((0,0),vars.resolution))    
        vars.dt = clock.tick(75)/1000


        
        
    