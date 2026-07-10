from sprites import *


def collision(collider,margin = 5):
    if True:
        # Checks if either the left or right side of the player is over the collider 
        if (
            player.right >= collider.left + margin and player.right <= collider.right 
            or player.left <= collider.right - margin and player.left >= collider.left ):
            
            #top side
            if player.bottom < collider.bottom and player.bottom >= collider.top +1 : 
                if player.accely > 0:
                    player.accely = 0
                if player.vely > 0:
                    player.vely = 0
                player.y = collider.top - player.height
                
            #bottom side
            elif player.top > collider.top and player.top <= collider.bottom +1:
                if player.accely < 0:
                    player.accely = 0
                if player.vely < 0:
                    player.vely = 0
                player.y = collider.bottom 
                
            
        # Checks if either the top or bottom side of the player is over the collider
        if (
            player.bottom >= collider.top + margin and player.bottom <= collider.bottom 
            or player.top <= collider.bottom - margin and player.top >= collider.top ):
            #left side
            if player.right < collider.right and player.right >= collider.left +1:
                if player.accelx > 0:
                    player.accelx = 0
                if player.velx > 0:
                    player.velx = 0
                player.x = collider.left-player.width

            #right side
            elif player.left > collider.left and player.left <= collider.right  :
                if player.accelx < 0: 
                    player.accelx = 0
                if player.velx < 0: 
                    player.velx = 0
                player.x = collider.right 


