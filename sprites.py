import pygame
import vars
import map

def center(size,pos):
    width = size[0]
    height = size[1]
    left = pos[0]
    top = pos[1]
    return (width/2+left,height/2+top)



class sprite:
    def __init__(self,pos,size,texture_name,vel = (0,0), accel = (0,0)):
        self.pos = pos
        self.vel = vel
        self.accel = accel
        self.size = size
        self.surface = pygame.transform.scale(pygame.image.load(texture_name),size)
        self.rect = pygame.Rect(pos,size)
    @property
    def pos(self):
        return (self.x, self.y)
    @pos.setter
    def pos(self,tuple):
        (self.x, self.y) = tuple
    @property
    def vel(self):
        return (self.velx , self.vely)
    @vel.setter
    def vel(self,vel):
        (self.velx , self.vely) = vel
    @property
    def accel(self):
        return (self.accelx , self.accely)
    @accel.setter
    def accel(self,accel):
        (self.accelx , self.accely) = accel
    @property
    def size(self):
        return (self.width, self.height)
    @size.setter
    def size(self, tuple):
        (self.width, self.height) = tuple
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

    def movement(self):


        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] == True: #and if vel < a vel and if on ground 
            self.vely = -500
        elif keys_pressed[pygame.K_s] == True: # increase max accel down
            self.accely = 500 
        else:
            self.accely = 0
        self.vely += self.accely* vars.dt 
        self.y += self.vely*vars.dt 

        #movement y
        if keys_pressed[pygame.K_a] == True: #
            self.accelx = -500
        elif keys_pressed[pygame.K_d] == True:
            self.accelx = 500     
        else:
            self.accelx = 0
        self.velx += self.accelx*vars.dt
        self.x += self.velx*vars.dt    
    
    def air_res(self):
        self.vel = [vel-vel*vars.dt*0.5 for vel in self.vel]

    def gravity(self):
        self.vely += 1000*vars.dt

player = sprite((800,500),(100,100),'boxplayer.webp',(0,0),(0,0))

class Camera(sprite):
    def __init__(self, pos, size, texture_name = 'Untitled.jpg', vel=(0,0), accel=(0,0)):
        super().__init__(pos, size, texture_name, vel, accel)

    def follow_player(self,player = player):
        x_dist = -self.x + (vars.screen_width / 2) - player.centerx 
        y_dist = -self.y + (vars.screen_height / 2) - player.centery
        if (x_dist) ** 2 + (y_dist) ** 2 >= 1000: #if the player is outside a certain radius from the center
            self.x+= x_dist*abs(x_dist)/10000
            self.y+= y_dist*abs(y_dist)/10000


    @property
    def display_part(self):
        screen = pygame.Rect((-self.x,-self.y),(vars.resolution))
        return(screen)
    @display_part.setter
    def display_part(self,tuple):
        self.pos = (tuple[0] , tuple[1])
        
camera = Camera((0,0),map.map_size) 



    







#create player









