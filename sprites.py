import pygame
import vars


dash_speed = 500
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
    def __init__(self,pos,size,texture_name,vel = (0,0), accel = (0,0)):
        self.pos = pos
        self.vel = vel
        self.accel = accel
        self.size = size
        self.surface = pygame.transform.scale(pygame.image.load(texture_name),size)
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



class Player(sprite):
    def __init__(self, pos, size, texture_name, vel=(0, 0), accel=(0, 0),input_direction = (0,0),vel_direction = (0,0)):
        super().__init__(pos, size, texture_name, vel, accel)
        self.input_direction = input_direction
        self.vel_direction = vel_direction
        self.dash_cooldown_time = 0
    @property
    def input_direction(self):
        return (self.input_directionx,self.input_directiony)
    @input_direction.setter
    def input_direction(self,tuple):
        (self.input_directionx,self.input_directiony) = tuple  

    def movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
            pass
        elif keys_pressed[pygame.K_UP]:
            self.input_directiony = -1
            if not self.colliding_top:
                self.jump()
            

        elif keys_pressed[pygame.K_DOWN]:
            self.input_directiony = 1
            if not self.colliding_bottom:
                self.accely = 500 
            

        else:
            self.accely = 0
            self.input_directiony = 0


        #movement y
        if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_RIGHT]:
            self.accelx = 0
        elif keys_pressed[pygame.K_LEFT]:
            self.input_directionx = -1
            if not self.colliding_right:
                self.accelx = -500

        elif keys_pressed[pygame.K_RIGHT] :   
            self.input_directionx = 1
            if not self.colliding_left:
                self.accelx = 500 

        else:
            self.accelx = 0
            self.input_directionx = 0
   
    

    
    def on_wall(self): 
        pass


    def air_res(self):
        self.vel = [vel-vel*vars.dt*0.5 for vel in self.vel]

    def gravity(self):
        self.vely += 1000*vars.dt     

    def update_movement(self):
        self.velx += self.accelx*vars.dt
        self.vely += self.accely*vars.dt
        self.x += self.velx*vars.dt
        self.y += self.vely*vars.dt
        self.vel_direction = tuple(map(sign,self.vel))
        if self.dash_cooldown_time <2:
            self.dash_cooldown_time += vars.dt
    def jump(self):
        if self.collided_bottom:
            self.vely = -500
            self.vel_directiony = -1
            self.collided_bottom = False #currently nothings happening
        else: 
            self.accely = -380

           

    def dash(self):
        print(self.dash_cooldown_time)
        if self.dash_cooldown_time > 1:
            if (self.input_directionx !=0 and 
                self.input_directiony !=0):
                if self.input_directionx != 0:
                    if sign(self.velx) == self.input_directionx:
                        self.velx += 500/root_2*self.input_directionx
                    else:
                        self.velx = 500/root_2*self.input_directionx
                if self.input_directiony != 0:
                    if sign(self.vely) == self.input_directiony:
                        self.vely += 500/root_2*self.input_directiony
                    else:
                        self.vely = 500/root_2*self.input_directiony
            else: 
                if self.input_directionx != 0:
                    if sign(self.velx) == self.input_directionx:
                        self.velx += 500*self.input_directionx
                    else:
                        self.velx = 500*self.input_directionx
                else:
                    self.velx = 500*self.input_directionx
                if self.input_directiony != 0:
                    if sign(self.vely) == self.input_directiony:
                        self.vely += 500*self.input_directiony
                    else:
                        self.vely = 500*self.input_directiony
                else:
                    self.vely = 500*self.input_directiony
            self.dash_cooldown()

    def dash_cooldown(self):
        self.dash_cooldown_time = 0

    def create_crumble(self,crumble_block):
        crumble_block.center = [x+y for x,y in zip(self.center,[direction*200 for direction in self.input_direction])]
        crumble_block.crumbled = False
        crumble_block.crumble_cooldown_time = 0
        crumble_block.crumbling = False
        crumble_block.collided_top = False
class crumble_block(sprite):
    def __init__(self, pos, size, texture_name, vel=(0, 0), accel=(0, 0)):
        super().__init__(pos, size, texture_name, vel, accel)
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
        
crumble = crumble_block((1536, 1040),(112, 16),'boxplayer.webp')
player = Player((800,500),(100,100),'boxplayer.webp')

    







#create player









