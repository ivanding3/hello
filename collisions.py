import vars



def overlapping(obj_1,obj_2,):
    # Checks if either the left or right side of the obj_1 is over the obj_2 
    if (obj_1.right >= obj_2.left  and obj_1.right <= obj_2.right or
        obj_1.left <= obj_2.right  and obj_1.left >= obj_2.left):
        if (obj_1.bottom < obj_2.bottom and obj_1.bottom >= obj_2.top  or
            obj_1.top > obj_2.top and obj_1.top <= obj_2.bottom ):
            return True


    # Checks if either the top or bottom side of the obj_1 is over the obj_2
    if (obj_1.bottom >= obj_2.top  and obj_1.bottom <= obj_2.bottom or
        obj_1.top <= obj_2.bottom  and obj_1.top >= obj_2.top):
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

    
def collision_left(obj,static_obj):
    if (obj.vel_directionx != 1 and
        obj.bottom > static_obj.top and 
        obj.top < static_obj.bottom and
        obj.left >= static_obj.right and
        obj.left + obj.velx*vars.dt <= static_obj.right):
            obj.collided_left = True
            static_obj.collided_right = True
            obj.left = static_obj.right
            obj.left_colliding.append(static_obj)

def collision_right(obj,static_obj):
    if (obj.vel_directionx != -1 and
        obj.bottom > static_obj.top and 
        obj.top < static_obj.bottom and
        obj.right <= static_obj.left and
        obj.right + obj.velx*vars.dt >= static_obj.left):
            obj.collided_right = True
            static_obj.collided_left = True
            obj.right = static_obj.left
            obj.right_colliding.append(static_obj)

def collision_top(obj,static_obj):
    if (obj.vel_directiony != 1 and
        obj.right > static_obj.left and 
        obj.left < static_obj.right and
        obj.top >= static_obj.bottom and
        obj.top + obj.vely*vars.dt <= static_obj.bottom):
            obj.collided_top = True
            static_obj.collided_bottom = True
            obj.top = static_obj.bottom
            obj.top_colliding.append(static_obj)
def collision_bottom(obj,static_obj):
    
    if (obj.vel_directiony != -1 and
        obj.right > static_obj.left and 
        obj.left < static_obj.right and
        obj.bottom <= static_obj.top and
        obj.bottom + obj.vely*vars.dt >= static_obj.top):
            obj.collided_bottom = True
            static_obj.collided_top = True
            obj.bottom = static_obj.top
            obj.bottom_colliding.append(static_obj)

def collision(obj,static_obj):
    collision_left(obj,static_obj)
    collision_right(obj,static_obj)
    collision_top(obj,static_obj)
    collision_bottom(obj,static_obj)

def check_colliding(obj):

    if len(obj.left_colliding) > 0:
        obj.colliding_left = True
    else:
        obj.colliding_left = False 
    if len(obj.right_colliding) > 0:
        obj.colliding_right = True 
    else:
         obj.colliding_right = False
    if len(obj.top_colliding) > 0:
        obj.colliding_top = True 
    else:
         obj.colliding_top = False
    if len(obj.bottom_colliding) > 0:
        obj.colliding_bottom = True
    else:
        obj.colliding_bottom = False
    obj.clear_colliders()
    
