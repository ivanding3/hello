from player_stuff import *

gravity = 1

def collision(collider,margin = 5):
    if True:
        # Checks if either the left or right side of the player is over the collider 
        if (
            player.right >= collider.rect.left + margin and player.right <= collider.rect.right 
            or player.left <= collider.rect.right - margin and player.left >= collider.rect.left ): 
            #top side
            if player.bottom < collider.rect.bottom and player.bottom >= collider.rect.top +1 : 
                if player.y_accel > 0:
                    player.y_accel = 0
                if player.y_vel > 0:
                    player.y_vel = 0
                player.y = collider.rect.top - player.img.get_height()
            
            #bottom side
            elif player.top > collider.rect.top and player.top <= collider.rect.bottom +1:
                if player.y_accel < 0:
                    player.y_accel = 0
                if player.y_vel < 0:
                    player.y_vel = 0
                player.y = collider.rect.bottom 
                
            
        # Checks if either the top or bottom side of the player is over the collider
        if (
            player.bottom >= collider.rect.top + margin and player.bottom <= collider.rect.bottom 
            or player.top <= collider.rect.bottom - margin and player.top >= collider.rect.top ):
            #left side
            if player.right < collider.rect.right and player.right >= collider.rect.left +1:
                if player.x_accel > 0:
                    player.x_accel = 0
                if player.x_vel > 0:
                    player.x_vel = 0
                player.x = collider.rect.left-player.img.get_width() 

            #right side
            elif player.left > collider.rect.left and player.x <= collider.rect.right  :
                if player.x_accel < 0: 
                    player.x_accel = 0
                if player.x_vel < 0: 
                    player.x_vel = 0
                player.x = collider.rect.right 


def physics():
    
    player.y_vel += gravity
    print(player.y_vel,player.y_accel)