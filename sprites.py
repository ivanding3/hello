import pygame

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

    def movement(self,dt):


        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] == True: #and if vel < a vel and if on ground 
            self.vely = -500
        elif keys_pressed[pygame.K_s] == True: # increase max accel down
            self.accely = 500 
        else:
            self.accely = 0
        self.vely += self.accely*dt 
        self.y += self.vely*dt 

        #movement y
        if keys_pressed[pygame.K_a] == True: #
            self.accelx = -500
        elif keys_pressed[pygame.K_d] == True:
            self.accelx = 500     
        else:
            self.accelx = 0
        self.velx += self.accelx*dt
        self.x += self.velx*dt    
    
    def air_res(self,dt):
        self.vel = [vel-vel*dt*0.5 for vel in self.vel]

    def gravity(self,dt):
        self.vely += 1000*dt




    


player = sprite((0,0),(100,100),'boxplayer.webp',(0,0),(0,0))




#create player









