import pygame
from sprites import *

screen_width = 1600
screen_height = 900
resolution = (screen_width,screen_height)

#map data idk
#grid size 16 px

map_size = (3200,1800)

class Camera(sprite):
    def __init__(self, pos, size, texture_name = 'Untitled.jpg', vel=(0,0), accel=(0,0)):
        super().__init__(pos, size, texture_name, vel, accel)

    def follow_player(self,player = player):
        x_dist = -self.x + (screen_width / 2) - player.centerx 
        y_dist = -self.y + (screen_height / 2) - player.centery
        if (x_dist) ** 2 + (y_dist) ** 2 >= 10000: #if the player is outside a certain radius from the center
            self.x+= x_dist/70
            self.y+= y_dist/70
            print(self.x,self.y)

    @property
    def display_part(self):
        screen = pygame.Rect((-self.x,-self.y),(resolution))
        return(screen)
    @display_part.setter
    def display_part(self,tuple):
        self.pos = (tuple[0] , tuple[1])
        
camera = Camera((0,0),map_size) 