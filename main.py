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

margin = 0


while True:
    pygame.display.flip()
    dt = clock.tick(1000)/1000
    keys_pressed = pygame.key.get_pressed()
    
    #movement x
    if keys_pressed[pygame.K_w] == True: #and if vel < a vel and if on ground
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
    if player_rect_col.bottom > floor_rect.top:
        print(player_rect_col.bottom, floor_rect.top)
        player.y_vel = 0
        player_rect_col.bottom = floor_rect.top
        player.y = player_rect_col.top
    #if player_rect_col.right 

    def collision(collider):
        collider.col_rect.center = collider.rect.center
        # Checks if either the left or right side of the player is over the collider 
        if (
            player_rect_col.right > collider.col_rect.left + margin and player_rect_col.left < collider.col_rect.right
            or player_rect_col.left < collider.col_rect.right - margin and player_rect_col.right>collider.col_rect.left): 
            #above
            if player_rect_col.centery < collider.col_rect.top and player_rect_col.bottom >= collider.col_rect.top:
                if player.y_accel > 0:
                    player.y_accel = 0
                if player.y_vel > 0:
                    player.y_vel = 0
                player.y = collider.col_rect.top - player.img.get_height() -1
            #below
            elif player_rect_col.centery > collider.col_rect.bottom and player_rect_col.top <= collider.col_rect.bottom:
                if player.y_accel < 0:
                    player.y_accel = 0
                if player.y_vel < 0:
                    player.y_vel = 0
                player.y = collider.col_rect.bottom 
        # Checks if either the top or bottom side of the player is over the collider
        if (
            player_rect_col.bottom > collider.col_rect.top + margin and player_rect_col.top < collider.col_rect.bottom
            or player_rect_col.top < collider.col_rect.bottom - margin and player_rect_col.bottom > collider.col_rect.top):
            #left
            if player_rect_col.centerx < collider.col_rect.left and player_rect_col.right >= collider.col_rect.left:
                if player.x_accel > 0:
                    player.x_accel = 0
                if player.x_vel > 0:
                    player.x_vel = 0
                player.x = collider.col_rect.left-player.img.get_width() -1
            #right
            elif player_rect_col.centerx > collider.col_rect.left and player_rect_col.left <= collider.col_rect.right:
                if player.x_accel < 0: 
                    player.x_accel = 0
                if player.x_vel < 0: 
                    player.x_vel = 0
                player.x = collider.col_rect.right 


    collision(random_obj)



    

    #updating positions

   


    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.pos = pygame.mouse.get_pos()  
    
#update
    player.pos = (player.x,player.y)
    player_rect_col.topleft = player.pos
#drawing
    screen.blit(background,(0,0))
    screen.blit(floor,(0,screen_height- floor.get_height()))
    #screen.blit(box,box_rect.topleft)
    screen.blit(random_obj.img,random_obj.rect)


    screen.blit(player.img, (player.pos))        
