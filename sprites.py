import pygame
import vars
from pathlib import Path

dash_speed = 600
dash_cd = 0.4
move_speed = 500
root_2 = 2**(1/2)

def center(size,pos):
    width = size[0]
    height = size[1]
    left = pos[0]
    top = pos[1]
    return (width/2+left,height/2+top)

def sign(num):
    if num > 0 :return 1
    if num < 0 :return-1
    if num == 0:return 0


class sprite:
    def __init__(self,pos,size,texture_name):
        self.pos = pos
        self.vel = (0,0)
        self.accel = (0,0)
        self.size = size
        self.surface = pygame.transform.scale(pygame.image.load(Path.cwd()/'assets'/texture_name),size)
        self.rect = pygame.Rect(pos,size)
        self.colliding_left = False
        self.colliding_right = False
        self.colliding_top = False
        self.collided_top = False
        self.colliding_bottom = False
        self.collided_bottom = False

    @property
    def pos(self):
        return (self.x,self.y)
    @pos.setter
    def pos(self,tuple):
        (self.x,self.y) = tuple
    @property
    def vel(self):
        return (self.velx,self.vely)
    @vel.setter
    def vel(self,vel):
        (self.velx,self.vely) = vel
    @property
    def accel(self):
        return (self.accelx,self.accely)
    @accel.setter
    def accel(self,accel):
        (self.accelx,self.accely) = accel
    @property
    def vel_direction(self):
        return (self.vel_directionx,self.vel_directiony)
    @vel_direction.setter
    def vel_direction(self,tuple):
        (self.vel_directionx,self.vel_directiony) = tuple  
    @property
    def size(self):
        return (self.width,self.height)
    @size.setter
    def size(self, tuple):
        (self.width,self.height) = tuple
    @property
    def left(self):
        return self.x
    @left.setter
    def left(self,val):   
        self.x = val
    @property
    def right(self):
        return self.x + self.width
    @right.setter
    def right(self,val):
        self.x = val - self.width
    @property
    def top(self):
        return self.y
    @top.setter
    def top(self,val):
        self.y = val
    @property
    def bottom(self):
        return self.y + self.height
    @bottom.setter
    def bottom(self,val):
        self.y = val - self.height
    @property
    def center(self):
        return (self.centerx,self.centery)
    @center.setter
    def center(self,tuple):
        (self.centerx,self.centery) = tuple
    @property
    def centerx(self):
        return self.width/2+self.left
    @centerx.setter
    def centerx(self,val):
        self.x = val-self.width/2
    @property
    def centery(self):
        return self.height/2+self.top
    @centery.setter
    def centery(self,val):
        self.y = val-self.height/2
    @property
    def midtop(self):
        return (self.x+self.width/2,self.y)
    @midtop.setter
    def midtop(self,tuple):
        (self.x,self.y)= (tuple[0]-self.width/2,tuple[1])
    @property
    def midbottom(self):
        return (self.x+self.width/2,self.y+self.height)
    @midbottom.setter
    def midbottom(self,tuple):
        (self.x,self.y)= (tuple[0]-self.width/2,tuple[1]+self.height)


class Player(sprite):
    def __init__(self, pos, size, texture_name):
        super().__init__(pos, size, texture_name)
        self.input_direction = (0,0)
        self.vel_direction = (0,0)
        self.dash_cooldown_time = 0
        self.gravity_enabled = True
        self.left_colliding = []
        self.right_colliding = []
        self.top_colliding = []
        self.bottom_colliding = []
        self.colliding_left = False
        self.colliding_right = False
        self.colliding_top = False
        self.colliding_bottom = False
        self.overlapping = False
        self.respawn_point = pos
        self.utils = 1
        self.in_dash = False
        self.dashx = 0
        self.dashy = 0
        self.facing = 1
        self.paused = False
        self.death_count = 0
    @property
    def respawn_point(self):
        return (self.respawn_x,self.respawn_y)
    @respawn_point.setter
    def respawn_point(self,tuple):
        (self.respawn_x,self.respawn_y) = tuple
    @property
    def input_direction(self):
        return (self.input_directionx,self.input_directiony)
    @input_direction.setter
    def input_direction(self,tuple):
        (self.input_directionx,self.input_directiony) = tuple  
    def clear_colliders(self):
        self.left_colliding = []
        self.right_colliding = []
        self.top_colliding = []
        self.bottom_colliding = []

    def move_left(self):
        self.accelx += -move_speed
    def move_right(self): 
        self.accelx += move_speed
    
    def jump(self):
        if self.colliding_bottom:
            self.vely = -700
            self.collided_bottom = False
        else:
            self.accely = -700
    
    def fast_fall(self):
        self.accely +=move_speed

    


    def friction(self):
        if self.colliding_bottom:
            if self.input_directionx != self.vel_directionx:
                if abs(self.velx) < 1:
                    self.velx = 0
                else:
                    self.velx -= 10*self.velx*vars.dt
    def on_wall(self): 
        pass


    def air_res(self):
        if self.input_directionx != self.vel_directionx and not self.colliding_bottom:
            self.velx -= 7*self.velx*vars.dt
        

    def gravity(self):
        if not self.colliding_bottom:
            self.vely += 1500*vars.dt     
    def collided(self):
        if (self.colliding_left or 
            self.colliding_right or 
            self.colliding_top or 
            self.colliding_bottom):
            return True

    def check_pause(self):
        
        if vars.load_time > 0: 
            self.paused = True
        else:
            self.paused = False
        if vars.load_time > -10:
            vars.load_time -= vars.dt

        

    def update_movement(self):

        self.friction()
        self.velx += self.accelx*vars.dt
        self.velx -= 1*self.velx*vars.dt#friction
        self.vely += self.accely*vars.dt
        if self.vel_directiony == -1:
            self.vely -= 1*self.vely*vars.dt
        self.air_res()
        self.accel = (0,0)
        self.vel_direction = tuple(map(sign,self.vel))
        if self.in_dash:
            self.accel = (0,0)
            self.vel = self.dashx,self.dashy
            player.surface = pygame.transform.scale(pygame.image.load(Path.cwd()/'assets'/'red.png'),(64,64))
        else:
            player.surface = pygame.transform.scale(pygame.image.load(Path.cwd()/'assets'/'boxplayer.png'),(64,64))
        if (self.colliding_left and self.vel_directionx == -1 or
            self.colliding_right and self.vel_directionx == 1):
            self.velx = 0
            self.in_dash = False
        if (self.colliding_top and self.vel_directiony == -1 or
            self.colliding_bottom and self.vel_directiony == 1):
            self.vely = 0
            self.in_dash = False
        if self.overlapping:
            self.in_dash = False


        self.x += self.velx*vars.dt
        self.y += self.vely*vars.dt
        if self.dash_cooldown_time < dash_cd +1:
            self.dash_cooldown_time += vars.dt
        if self.dash_cooldown_time >= dash_cd:
            self.in_dash = False    
        if self.gravity_enabled:
            self.gravity()


            


           

    def dash(self):
        
        if self.dash_cooldown_time > dash_cd and self.utils > 0:
            init_velx = self.velx
            init_vely = self.vely
            self.in_dash = True
            if self.input_direction == (0, 0):
                self.dashy = 0
                if sign(init_velx) != self.facing*-1:
                    self.dashx = init_velx + dash_speed*self.facing
                else:
                    self.dashx = dash_speed*self.facing
            else:
                if self.input_directionx == 0 : 
                    self.dashx = 0
                elif self.input_directiony == 0:
                    self.dashy = 0
            if (self.input_directionx !=0 and 
                self.input_directiony !=0):
                    if sign(init_velx) != self.input_directionx*-1:
                        self.dashx = init_velx + dash_speed/root_2*self.input_directionx
                    else:
                        self.dashx = dash_speed/root_2*self.input_directionx

                    if sign(init_vely) != self.input_directiony*-1:
                        self.dashy = init_vely+dash_speed/root_2*self.input_directiony
                    else:
                        self.dashy = dash_speed/root_2*self.input_directiony
            else: 
                if self.input_directionx != 0:
                    if sign(init_velx) != self.input_directionx*-1:
                        self.dashx = init_velx + dash_speed*self.input_directionx
                    else:
                        self.dashx = dash_speed*self.input_directionx
                if self.input_directiony != 0:
                    if sign(init_vely) != self.input_directiony*-1:
                        self.dashy =  init_vely + dash_speed*self.input_directiony
                    else:
                         self.dashy = dash_speed*self.input_directiony



            self.utils -= 1
            self.dash_cooldown_time = 0.0
        

    def create_crumble(self,crumble_block):
        if self.utils > 0:
            if self.input_direction != (0,0):
                crumble_block.center = (self.centerx + self.input_directionx*200,
                                        self.centery + self.input_directiony*200)
            else:
                crumble_block.center = (self.centerx + self.facing*200,
                                        self.centery + self.input_directiony*200)
            crumble_block.crumbled = False
            crumble_block.crumble_cooldown_time = 0
            crumble_block.crumbling = False
            crumble_block.collided_top = False
            self.utils -= 1

    def reset_util(self):
        self.utils = 1

    def death_animation(self):
        ...
    def die(self):
        self.death_animation()
        self.accel = (0,0)
        self.vel = (0,0)
        self.pos = self.respawn_point
        self.in_dash = False
        crumble.pos = (-10000,10000)
        self.death_count += 1
class crumble_block(sprite):
    def __init__(self, pos, size, texture_name):
        super().__init__(pos, size, texture_name)
        self.crumble_time = 1
        self.crumble_cooldown_time = 0
        self.crumbled = False
        self.crumbling = False

    def crumble_animation(self):
        ...       
    def crumble(self):
        if not self.crumbling:
            self.crumble_animation()
            self.crumbling = True
        else:
            self.update_crumble()
            if self.crumble_cooldown_time > self.crumble_time:
                self.crumbled = True
                self.crumble_cooldown_time = 0
                self.collided_top = False
                
    def update_crumble(self):
        self.crumble_cooldown_time += vars.dt


crumble = crumble_block((-1000, 1040),(160, 160),'box.png')
player = Player((800,500),(64,64),'boxplayer.png')









#create player









