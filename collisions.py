import sprites
import vars



def overlapping(obj_1,obj_2,margin = 2):
    if obj_1 == sprites.player:
        margin = 5
    # Checks if either the left or right side of the obj_1 is over the obj_2 
    if (obj_1.right >= obj_2.left + margin and obj_1.right <= obj_2.right or
        obj_1.left <= obj_2.right - margin and obj_1.left >= obj_2.left):
        if (obj_1.bottom < obj_2.bottom and obj_1.bottom >= obj_2.top  or
            obj_1.top > obj_2.top and obj_1.top <= obj_2.bottom ):
            return True


    # Checks if either the top or bottom side of the obj_1 is over the obj_2
    if (obj_1.bottom >= obj_2.top + margin and obj_1.bottom <= obj_2.bottom or
        obj_1.top <= obj_2.bottom - margin and obj_1.top >= obj_2.top):
        if (obj_1.right < obj_2.right and obj_1.right >= obj_2.left  or
            obj_1.left > obj_2.left and obj_1.left <= obj_2.right):
            return True
    return False
#returns axis and value closest to 0 and 
def sort_closest(dists): 
    dists = list(enumerate(dists))
    closest = []
    for i in range(len(dists)):
        closest.append((abs(dists[i][1]),dists[i][0]))
    return dists[sorted(closest)[0][1]]


     



def collision(collider,margin = 5):
        # Checks if either the left or right side of the player is over the collider 
        if (sprites.player.right >= collider.left + vars.margin and sprites.player.right <= collider.right or
            sprites.player.left <= collider.right - vars.margin and sprites.player.left >= collider.left ):
            
            #top side
            if sprites.player.bottom < collider.bottom and sprites.player.bottom >= collider.top  : 
                pass
                if sprites.player.accely > 0:
                    sprites.player.accely = 0
                if sprites.player.vely > 0:
                    sprites.player.vely = 0
                sprites.player.y = collider.top - sprites.player.height
                print("top")
            #bottom side
            elif sprites.player.top > collider.top and sprites.player.top <= collider.bottom:
                if sprites.player.accely < 0: 
                    sprites.player.accely = 0
                if sprites.player.vely < 0:
                    sprites.player.vely = 0
                sprites.player.y = collider.bottom 
                print("bottom")
            
        # Checks if either the top or bottom side of the sprites.player is over the collider
        if (sprites.player.bottom >= collider.top + vars.margin and sprites.player.bottom <= collider.bottom or
            sprites.player.top <= collider.bottom - vars.margin and sprites.player.top >= collider.top ):
            #left side
            if sprites.player.right < collider.right and sprites.player.right >= collider.left:
                if sprites.player.accelx > 0:
                    sprites.player.accelx = 0
                if sprites.player.velx > 0:
                    sprites.player.velx = 0
                sprites.player.x = collider.left-sprites.player.width
                print("left")
            #right side
            elif sprites.player.left > collider.left and sprites.player.left <= collider.right:
                if sprites.player.accelx < 0: 
                    sprites.player.accelx = 0
                if sprites.player.velx < 0: 
                    sprites.player.velx = 0
                sprites.player.x = collider.right 
                print(sprites.player.velx ,sprites.player.accelx )


