import pygame
import sprites
import vars


#map data idk
#grid size 16 px

map_size = (6400,1800)

map_objects = []

def snap_to_grid(pos,size = 16):
    return (round(pos[0]/size)*size,round(pos[1]/size)*size)

class Camera(sprites.sprite):
    def __init__(self, pos, size, texture_name = 'Untitled.jpg', vel=(0,0), accel=(0,0)):
        super().__init__(pos, size, texture_name, vel, accel)

    def follow_player(self,player = sprites.player):
        x_dist = -self.x + (vars.screen_width / 2) - player.centerx 
        y_dist = -self.y + (vars.screen_height / 2) - player.centery
        if (x_dist) ** 2 + (y_dist) ** 2 >= 1000: #if the player is outside a certain radius from the center
            self.x+= x_dist*abs(x_dist)/10000
            self.y+= y_dist*abs(y_dist)/10000
        self.x -= player.velx/70
        self.y -= player.vely/70


    @property
    def display_part(self):
        screen = pygame.Rect((-self.x,-self.y),(vars.resolution))
        return(screen)
    @display_part.setter
    def display_part(self,tuple):
        self.pos = (tuple[0] , tuple[1])
        
camera = Camera((0,0),map_size)


#map maker
class Map_maker():
    def __init__(self):
        self.creating = False
        self.obj_count = 0
    

    def create_obj(self):
        if self.creating:
            self.init()
            self.display_ghost()
            
        
    def initializing(self,event):
        self.init = snap_to_grid([x-y for x,y in zip(event.pos,camera.pos)])
        self.creating = True


    def display_ghost(self):
        size = [y-x for x,y in zip(self.init,[x-y for x,y in zip(pygame.mouse.get_pos(),camera.pos)])]
        camera.surface.fill((00,00,00),pygame.Rect(self.init,size))
    
    def finalizing(self,event):
        break_it = False
        self.final = snap_to_grid([x-y for x,y in zip(event.pos,camera.pos)])
        self.size = tuple([y-x for x,y in zip(self.init,self.final)])
        for length in self.size:
            if length <0:
                self.creating = False
                break_it = True
        if break_it:
            return None      
        with open('map_objs.txt','a') as f:
            f.write(f"{self.init}/{self.size}/Green.webp/sprite_{self.obj_count}/\n")
            self.obj_count+=1
            self.creating = False            
    def map_mode(self):
        if self.creating:
            self.display_ghost()
  

map_maker = Map_maker()  

    



    
    


         














random_obj = sprites.sprite((1000,500),(100,100),'Green.webp')





floor = sprites.sprite((0,700),(16000,200),'Green.webp')
