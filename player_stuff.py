import pygame


def center(size,pos):
    width = size[0]
    height = size[1]
    left = pos[0]
    top = pos[1]
    return (width/2+left,height/2+top)



class Player:
    def __init__(self,player_x,player_y,player_x_vel,player_y_vel,player_x_accel,player_y_accel,img,width,height):
        self.x = player_x
        self.y = player_y
        self.x_vel = player_x_vel
        self.y_vel = player_y_vel
        self.x_accel = player_x_accel
        self.y_accel = player_y_accel
        self.img = img
        self.width = width
        self.height = height

    @property
    def pos(self):
        return (self.x, self.y)
    @pos.setter
    def pos(self,tuple):
        (self.x, self.y) = tuple
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
        self.y = val - self.width
    





    


player = Player(500,500,0,0,0,0,pygame.transform.scale(pygame.image.load('boxplayer.webp'), (100,100)),100,100)




#create player









