import pygame


def center(size,pos):
    width = size[0]
    height = size[1]
    left = pos[0]
    top = pos[1]
    return (width/2+left,height/2+top)

class Player:
    def __init__(self,player_x,player_y,player_pos,player_x_vel,player_y_vel,player_x_accel,player_y_accel,img):
        self.x = player_x
        self.y = player_y
        self.pos = player_pos
        self.x_vel = player_x_vel
        self.y_vel = player_y_vel
        self.x_accel = player_x_accel
        self.y_accel = player_y_accel
        self.img = img



player = Player(0,0,(0,0),0,0,0,0,pygame.transform.scale(pygame.image.load('boxplayer.webp'), (100,100)))



#player = pygame.transform.scale(pygame.image.load('boxplayer.webp'), (100,100))
player_rect_col = pygame.Rect((0,0),(player.img.get_width(),player.img.get_height()))
player_rect_col.center = center((100,100),(player.pos))
