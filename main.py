import pygame
from sys import exit
import sprites 
import ui 
import collisions 
import map_stuff 
import vars 
#menu screen still not done
#hitboxes for map mkaing
#implement mechanics ****
#create some gameplay
#needs last input direction
#last created shape is sticky from the left and right??
#coyote time
#needs util counter
#seperate movement method into seperate methods
clock = pygame.time.Clock()

pygame.display.init()


background = pygame.transform.scale(pygame.image.load('BG image.png'),(map_stuff.map_size))


file_len = 0



pygame.event.set_blocked(pygame.MOUSEMOTION)

frame = 0


game_running = True
while game_running:
    frame +=1
    #print(frame)
    margin = (sum(map(abs,sprites.player.vel))//30)
    if margin>5:
        vars.margin = margin
    
    keys_pressed = pygame.key.get_pressed()
    
    #print(f'fps = {1/vars.dt}')

    #print(player.vel,player.accel,dt)
    sprites.player.movement()
    

    map_stuff.camera.follow_player()

    #camera
    sprites.player.update_movement()
    sprites.player.air_res()
    sprites.player.gravity()
    


    
    #inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if ui.debug_button.pressed:
                sprites.player.pos = (pygame.mouse.get_pos()[0] - map_stuff.camera.x,
                                        pygame.mouse.get_pos()[1] - map_stuff.camera.y)
            if ui.map_mode_button.pressed:
                map_stuff.map_maker.initializing(event)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if ui.map_mode_button.pressed:
                map_stuff.map_maker.finalizing(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                sprites.player.dash()
            if event.key == pygame.K_z:
                sprites.player.create_crumble(sprites.crumble)
         

    


#drawing
    map_stuff.camera.surface.blit(background,(0,0))

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
                                                               
                
            






    map_stuff.camera.surface.blit(sprites.player.surface, (sprites.player.pos))
    if ui.map_mode_button.pressed:
        map_stuff.map_maker.map_mode()

        for i in range(map_stuff.map_size[0]//16):
            pygame.draw.line(map_stuff.camera.surface,(200,200,200),(i*16,0),(i*16,map_stuff.map_size[1]))
        for i in range(map_stuff.map_size[1]//16):
            pygame.draw.line(map_stuff.camera.surface,(200,200,200),(0,i*16),(map_stuff.map_size[0],i*16))

    for collider_obj in map_stuff.map_objects:
        map_stuff.camera.surface.blit(collider_obj.surface,collider_obj.pos)
        collisions.collision(sprites.player,collider_obj)

   
     
    #crumble
    if sprites.crumble.collided_top:
        sprites.crumble.crumble()
    if not sprites.crumble.crumbled:
        collisions.collision(sprites.player,sprites.crumble)
        map_stuff.camera.surface.blit(sprites.crumble.surface,sprites.crumble.pos)

    vars.screen.blit(map_stuff.camera.surface,(0,0),map_stuff.camera.display_part)
    



    ui.test_button.run_button()
    ui.debug_button.run_button()
    ui.map_mode_button.run_button()


    pygame.display.update(pygame.Rect((0,0),vars.resolution))    
    vars.dt = clock.tick(75)/1000
    #print(sprites.player.accel,sprites.player.vel,sprites.player.pos)