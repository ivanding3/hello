import pygame
import sprites
import vars


#map data idk
#grid size 16 px

map_size = (6400,1800)

class Camera(sprites.sprite):
    def __init__(self, pos, size, texture_name = 'Untitled.jpg', vel=(0,0), accel=(0,0)):
        super().__init__(pos, size, texture_name, vel, accel)

    def follow_player(self,player = sprites.player):
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
        
camera = Camera((0,0),map_size)





random_obj = sprites.sprite((1000,500),(100,100),'Green.webp')


floor = sprites.sprite((0,700),(16000,200),'Green.webp')
