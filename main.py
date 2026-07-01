import pygame
from sys import exit
from player import *
from collisions import *

screen_width = 1600
screen_height = 900
resolution = (screen_width,screen_height)

clock = pygame.time.Clock()

pygame.display.init()
screen = pygame.display.set_mode((resolution),vsync=1)

background = pygame.transform.scale(pygame.image.load('Untitled.jpg'),(resolution))


box = pygame.transform.scale(pygame.image.load('Green.webp'),(200,200))
box_rect = pygame.Rect((1000,500),(200,200))

floor = pygame.transform.scale(pygame.image.load('Green.webp'),(screen_width,200))
floor_rect = pygame.Rect((0,screen_height-200),(floor.get_size()))

margin = 5



while True:
    
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

        
  



    #collisions??
    if player.bottom > floor_rect.top:
        print(player.bottom, floor_rect.top)
        player.y_vel = 0
        player.bottom = floor_rect.top
        player.y = player.top
    #if player.right 

    def collision(collider):
        if True:
            # Checks if either the left or right side of the player is over the collider 
            if (
                player.right >= collider.col_rect.left + margin and player.right <= collider.col_rect.right 
                or player.left <= collider.col_rect.right - margin and player.left >= collider.col_rect.left ): 
                #top side
                if player.bottom < collider.col_rect.bottom and player.bottom >= collider.col_rect.top +1 : 
                    if player.y_accel > 0:
                        player.y_accel = 0
                    if player.y_vel > 0:
                        player.y_vel = 0
                    player.y = collider.col_rect.top - player.img.get_height()
                   
                #bottom side
                elif player.top > collider.col_rect.top and player.top <= collider.col_rect.bottom +1:
                    if player.y_accel < 0:
                        player.y_accel = 0
                    if player.y_vel < 0:
                        player.y_vel = 0
                    player.y = collider.col_rect.bottom 
                    
                
            # Checks if either the top or bottom side of the player is over the collider
            if (
                player.bottom >= collider.col_rect.top + margin and player.bottom <= collider.col_rect.bottom 
                or player.top <= collider.col_rect.bottom - margin and player.top >= collider.col_rect.top ):
                #left side
                if player.right < collider.col_rect.right and player.right >= collider.col_rect.left +1:
                    if player.x_accel > 0:
                        player.x_accel = 0
                    if player.x_vel > 0:
                        player.x_vel = 0
                    player.x = collider.col_rect.left-player.img.get_width() 

                #right side
                elif player.left > collider.col_rect.left and player.x <= collider.col_rect.right  :
                    if player.x_accel < 0: 
                        player.x_accel = 0
                    if player.x_vel < 0: 
                        player.x_vel = 0
                    player.x = collider.col_rect.right 
    print(player.x , player.left)
    gravity = 1
    def physics():
        
        player.y_vel += gravity
        print(player.y_vel,player.y_accel)
    collision(random_obj)
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
    screen.blit(floor,(0,screen_height- floor.get_height()))
    #screen.blit(box,box_rect.topleft)
    screen.blit(random_obj.img,random_obj.rect)


    screen.blit(player.img, (player.pos))    
    pygame.display.flip()    
