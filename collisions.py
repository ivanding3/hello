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


     
def collided_left(obj,static_obj):
    if (obj.right == static_obj.left and 
        obj.bottom > static_obj.top and 
        obj.top < static_obj.bottom):
        return True
    else:
        return False
                 
def collider_left(obj,static_obj):
    if (obj.right < static_obj.left + vars.margin and
        obj.vel_directionx != -1 and
        obj.bottom > static_obj.top and 
        obj.top < static_obj.bottom and
        obj.right >= static_obj.left):
            obj.right = static_obj.left
            if obj.vel_directionx == 1:
                obj.velx = 0
                obj.accelx = 0

def collided_right(obj,static_obj):
    if (obj.left == static_obj.right and
        obj.bottom > static_obj.top and 
        obj.top < static_obj.bottom):
        return True
    else:
        return False
                 

def collider_right(obj,static_obj):
    if (obj.left > static_obj.right - vars.margin and
        obj.vel_directionx !=1 and
        obj.bottom > static_obj.top and 
        obj.top < static_obj.bottom and
        obj.left <= static_obj.right):
            obj.left = static_obj.right
            if obj.vel_directionx == -1:
                obj.velx = 0
                obj.accelx = 0
def collided_top(obj,static_obj):
    if (obj.bottom == static_obj.top and
        obj.right > static_obj.left and 
        obj.left < static_obj.right):
        return True
    else:
        return False

                
def collider_top(obj,static_obj):
    if (obj.bottom < static_obj.top + vars.margin and
        obj.vel_directiony != -1 and
        obj.right > static_obj.left and 
        obj.left < static_obj.right and
        obj.bottom >= static_obj.top):
            obj.bottom = static_obj.top
            obj.vely = 0
            obj.accely = 0

def collided_bottom(obj,static_obj):
    if (obj.top == static_obj.bottom and 
        obj.right > static_obj.left and 
        obj.left < static_obj.right):
        return True
    else:
        return False
                
def collider_bottom(obj,static_obj):

    if (obj.top > static_obj.bottom - vars.margin and
        obj.vel_directiony !=1 and
        obj.right > static_obj.left and 
        obj.left < static_obj.right and
        obj.top <= static_obj.bottom):
            obj.top = static_obj.bottom
            obj.vely = 0    
            obj.accely = 0





def collision(obj,static_obj):
    #left side of  static obj
    if collided_left(obj,static_obj):
        obj.right = static_obj.left
        #right side of obj
        obj.colliding_right = True
        static_obj.colliding_left = True
        obj.velx = 0
        obj.accelx = 0
    else:
        collider_left(obj,static_obj)
        obj.colliding_right = False
        static_obj.colliding_left = False
    
    if collided_right(obj,static_obj):
        obj.left = static_obj.right
        obj.colliding_left = True
        static_obj.colliding_right = True
        obj.velx = 0
        obj.accelx = 0      
    else:
        collider_right(obj,static_obj)
        obj.colliding_left = False
        static_obj.colliding_right = False

    if collided_top(obj,static_obj):
        obj.bottom = static_obj.top
        obj.collided_bottom = True
        obj.colliding_bottom = True
        static_obj.collided_top = True
        obj.vely = 0
        obj.accely = 0
    else:
        collider_top(obj,static_obj)
        obj.colliding_bottom = False
        static_obj.colliding_top = False


    if collided_bottom(obj,static_obj):
        obj.top = static_obj.bottom
        obj.colliding_top = True
        static_obj.colliding_bottom = True
        obj.vely = 0   
        obj.accely = 0
    else:
        collider_bottom(obj,static_obj)
        obj.colliding_top = False
        static_obj.colliding_bottom = False




