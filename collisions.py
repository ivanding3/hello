import pygame
from player import *
class collider:
    def __init__(self,rect,img,col_rect):
        self.rect = rect
        self.img = img
        self.col_rect = col_rect

def center(size,pos):
    width = size[0]
    height = size[1]
    left = pos[0]
    top = pos[1]
    return (width/2+left,height/2+top)

random_obj : collider = collider(pygame.Rect((1000,500),(100,100)),pygame.transform.scale(pygame.image.load('Green.webp'),(100,100)),pygame.Rect((1000,500),(99,99)))
random_obj.rect = random_obj.rect.move(0,0)




