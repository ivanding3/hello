import pygame
from player_stuff import *
class collider:
    def __init__(self,rect,img):
        self.rect = rect
        self.img = img


def center(size,pos):
    width = size[0]
    height = size[1]
    left = pos[0]
    top = pos[1]
    return (width/2+left,height/2+top)

random_obj = collider(pygame.Rect((1000,500),(100,100)),pygame.transform.scale(pygame.image.load('Green.webp'),(100,100)))
floor = collider(pygame.Rect((0,700),(1600,200)),pygame.transform.scale(pygame.image.load('Green.webp'),(1600,200)))




