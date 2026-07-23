import pygame
import sprites
import collisions
import vars
import ui
import json
from pathlib import Path
#map data idk
#grid size 16 px
#needs to be divisible by 16
map_size = (1920,1088)

map_objects = []

background = pygame.transform.scale(pygame.image.load(Path.cwd()/'assets'/'BG image.png'),(3200,3200))
background = pygame.Surface.convert(background)


class Room():
    def __init__(self,size,room_pos):
        self.size = size
        self.pos = room_pos
        self.room_key = str(room_pos)
        self.objs = []
        self.spikes = []
        self.loaders = []


    def update_room_objs(self):
        self.room = map_objs[main_camera.room_key]
        self.objs = map_objs[main_camera.room_key]['objs']
        self.spikes = map_objs[main_camera.room_key]['spikes']
        self.loaders = map_objs[main_camera.room_key]['loaders']

    @property
    def pos(self):
        return (self.x,self.y)
    @pos.setter
    def pos(self,tuple):
        (self.x,self.y) = tuple

    def update_room(self):
        for obj in self.objs:
            main_camera.surface.blit(obj.surface,obj.pos)
            collisions.collision(sprites.player,obj)
        for spike in self.spikes:
            spike.update()
        for loader in self.loaders:
            loader.check_overlap()


map_objs = {
    '(0, 0)': {
            'room' : Room((3200,1600),(0, 0)),
            'objs': [],
            'spikes': [],
            'loaders': [],
            }
}

def str_to_tuple(str):
    nums = []
    for i in range(len(str)):
        if str[i].isnumeric():
            if str[i-1] == '-':
                nums.append(-int(str[i]))
            else:
                nums.append(int(str[i]))
    return tuple(nums)

def snap_to_grid(pos,size = 16):
    return (round(pos[0]/size)*size,round(pos[1]/size)*size)

class Camera(sprites.sprite):
    def __init__(self, pos, size,texture_name = "Untitled.jpg"):
        super().__init__(pos,size,texture_name)
        self.surface = pygame.Surface(size)
        self.surface.fill((12,34,56))
        self.surface.set_colorkey((12,34,56))
        self.room_key = '(0, 0)'
        self.curr_room = map_objs[self.room_key]['room']
        self.background = background
    def follow_player(self,player = sprites.player):
        x_dist = -self.x + (vars.screen_width / 2) - player.centerx 
        y_dist = -self.y + (vars.screen_height / 2) - player.centery
        if (x_dist) ** 2 + (y_dist) ** 2 >= 1000: #if the player is outside a certain radius from the center
            self.x+= x_dist*abs(x_dist)/10000
            self.y+= y_dist*abs(y_dist)/10000
        self.x -= player.velx/50
        self.y -= player.vely/50

    def enter_new_room(self,room):
        self.pos = (-sprites.player.x + vars.screen_width//2,-sprites.player.y + vars.screen_height//2)
        self.size = room.size
        self.surface = pygame.Surface(self.size)
        self.surface.fill((12,34,56))
        self.surface.set_colorkey((12,34,56))
        self.curr_room = room
        self.room_key = str(self.curr_room.pos)
        self.curr_room.update_room_objs()
        self.background = pygame.transform.scale(self.background,room.size)
    
    def stay_in_room(self):
        if self.x > 0:
            self.x = 0
        elif -self.x > self.curr_room.size[0]-vars.screen_width:
            self.x = -self.curr_room.size[0]+vars.screen_width
        if self.y > 0:
            self.y = 0 
        elif -self.y > self.curr_room.size[1]-vars.screen_height:
            self.y  = -self.curr_room.size[1]+vars.screen_height

  



    @property
    def display_part(self):
        screen = pygame.Rect((-self.x,-self.y),(vars.resolution))
        return(screen)
    @display_part.setter
    def display_part(self,tuple):
        self.pos = (tuple[0] , tuple[1])







class loading_zone(sprites.sprite):
    def __init__(self, pos, size,room,texture_name='Untitled.jpg'):
        super().__init__(pos, size, texture_name)
        self.room = room
        self.surface = pygame.Surface(size)
        self.surface.fill((12,34,56))
        self.surface.set_colorkey((12,34,56))
        self.linked_loader = None
        self.loader_linked = False
        #1,2,3,4 correspond to left,top,right,bottom

    def init_loaders(self):
        if self.left == 0:
            self.room_side = 1
            linked_room_pos = (self.room.x-1,self.room.y)
            map_objs.setdefault(str(linked_room_pos) , {'room' : Room((map_size),linked_room_pos),
                                                'objs': [],
                                                'spikes': [],
                                                'loaders': [],
                                                })
            self.linked_room = map_objs[str(linked_room_pos)]['room']
        elif self.right == self.room.size[0]:
            self.room_side = 3
            linked_room_pos = (self.room.x+1,self.room.y)
            map_objs.setdefault(str(linked_room_pos) , {'room' : Room((map_size),linked_room_pos),
                                                'objs': [],
                                                'spikes': [],
                                                'loaders': [],
                                                })
            self.linked_room = map_objs[str(linked_room_pos)]['room']
        elif self.top == 0:
            self.room_side = 2
            linked_room_pos = (self.room.x,self.room.y+1)
            map_objs.setdefault(str(linked_room_pos) , {'room' : Room((map_size),linked_room_pos),
                                                'objs': [],
                                                'spikes': [],
                                                'loaders': [],
                                                })
            self.linked_room = map_objs[str(linked_room_pos)]['room']

        elif self.bottom == self.room.size[1]:
            self.room_side = 4
            linked_room_pos = (self.room.x,self.room.y-1)
            map_objs.setdefault(str(linked_room_pos) , {'room' : Room((map_size),linked_room_pos),
                                                'objs': [],
                                                'spikes': [],
                                                'loaders': [],
                                                })
            self.linked_room = map_objs[str(linked_room_pos)]['room']

    def link_loaders(self):
        for loader in map_objs[self.linked_room.room_key]['loaders']:
            loader.init_loaders()
            if (loader.room_side == self.room_side+2 or 
                loader.room_side == self.room_side-2 ):
                self.linked_loader = loader
                self.linked_loader.linked_loader = self
                self.loader_linked = True
                self.linked_loader.loader_linked = True
    def loading_animation(self):
        ...

    def load_linked_area(self):
        if self.loader_linked == False:
            self.link_loaders()
        if self.linked_loader == None:
            sprites.player.center = (400,400)
        elif self.room_side%2 == 1:
            if self.room_side == 1:
                sprites.player.right = self.linked_loader.left - 65
                sprites.player.respawn_x = self.linked_loader.left - 65
            else:
                sprites.player.left = self.linked_loader.right + 65
                sprites.player.respawn_x = self.linked_loader.right + 65
            sprites.player.bottom = self.linked_loader.bottom
            sprites.player.respawn_y = self.linked_loader.bottom-65
        else:
            if self.room_side == 2:
                sprites.player.bottom = self.linked_loader.top - 65
                sprites.player.respawn_y = self.linked_loader.top- 65
                #maybe give some vel
            else:
                sprites.player.top = self.linked_loader.bottom + 65
                sprites.player.respawn_y = self.linked_loader.bottom + 65
            sprites.player.centerx = self.linked_loader.centerx
            sprites.player.respawn_x = self.linked_loader.centerx - 32
        #camera stuff
        main_camera.enter_new_room(self.linked_room)
        if not self.loader_linked:
            self.link_loaders()

    def check_overlap(self):
        if collisions.overlapping(sprites.player,self):
            self.loading_animation()
            self.load_linked_area()


class Spike(sprites.sprite):
    def __init__(self, pos, size, texture_name):
        super().__init__(pos, size, texture_name)
        
    def update(self):                                        #fix clearing the speed/accel/other things that shouldnt transfer over
        if collisions.overlapping(sprites.player,self): 
            sprites.player.die()









main_camera = Camera((0,0),map_objs['(0, 0)']['room'].size)


#map maker
class Map_maker():
    def __init__(self):
        self.creating = False
        self.curr_room = map_objs[main_camera.room_key]['room']

    def save_map(self):
        with open('map_objs.json','w') as f:
            json.dump(map_objs_to_json(),f,indent= 2)
    
    def load_map(self):
        with open('map_objs.json','r') as f:
            a_dict = json.load(f)
            keys = []
            for key in a_dict:
                keys.append(key)
                map_objs.setdefault(key,{
                                    'room' : None,
                                    'objs': [],
                                    'spikes': [],
                                    'loaders': [],
                                    })
            for key in keys:
                map_objs[key]['room'] = Room(a_dict[key]['room']['size'],str_to_tuple(key))

                objs = []
                for obj in a_dict[key]['objs']:
                    objs.append(sprites.sprite(obj['pos'],obj['size'],obj['texture_name']))
                map_objs[key]['objs'] = objs

                spikes = []
                for spike in a_dict[key]['spikes']:
                    spikes.append(Spike(spike['pos'],spike['size'],spike['texture_name']))
                map_objs[key]['spikes'] = spikes

                loaders = []
                for loader in a_dict[key]['loaders']:

                    loaders.append(loading_zone(loader['pos'],loader['size'],Room(loader['room_size'],loader['room_pos']),texture_name=loader['texture_name']))
                    loading_zone(loader['pos'],loader['size'],Room(loader['room_size'],loader['room_pos']),texture_name=loader['texture_name']).init_loaders()
                map_objs[key]['loaders'] = loaders
            
    def find_curr_room(self):
        self.curr_room = map_objs[main_camera.room_key]['room']
    
    def curr_obj_type(self):
        for button in ui.map_subbuttons:
            if button.pressed:
                self.obj_type = button.type
    def create_obj(self):
        if self.creating:
            self.initializing()
            self.display_ghost()

        
    def initializing(self,event):
        self.init = snap_to_grid([x-y for x,y in zip(event.pos,main_camera.pos)])
        self.creating = True


    def display_ghost(self):
        self.size = [y-x for x,y in zip(self.init,[x-y for x,y in zip(pygame.mouse.get_pos(),main_camera.pos)])]
        main_camera.surface.fill((00,00,00),pygame.Rect(self.init,snap_to_grid(self.size)))
        
    
    def finalizing(self,event):
        break_it = False
        self.final = snap_to_grid([x-y for x,y in zip(event.pos,main_camera.pos)])
        self.size = tuple([y-x for x,y in zip(self.init,self.final)])
        for length in self.size:
            if length <1:
                self.creating = False
                break_it = True
        if break_it:
            return    
        self.creating = False 


        if self.obj_type == 'obj':
            map_objs[main_camera.room_key]['objs'].append(sprites.sprite(self.init,snap_to_grid(self.size),texture_name='Green.webp'))
        if self.obj_type == 'spike':
            map_objs[main_camera.room_key]['spikes'].append(Spike(self.init,snap_to_grid(self.size),texture_name='crowbox.png'))
        if self.obj_type == 'loader':
            loader = loading_zone((self.init),snap_to_grid(self.size),main_camera.curr_room)
            map_objs[main_camera.room_key]['loaders'].append(loader)
            loader.init_loaders()
        self.curr_room.update_room_objs()
        self.save_map()


    def map_mode(self):
 
        for event in vars.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                map_maker.initializing(event)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if map_maker.creating:
                    map_maker.finalizing(event)
        if self.creating:
            self.display_ghost()
    def over_obj(self,obj):
        if (
        pygame.mouse.get_pos()[0]-main_camera.x >= obj.pos[0] and pygame.mouse.get_pos()[1]-main_camera.y >= obj.pos[1] and 
        pygame.mouse.get_pos()[0]-main_camera.x <= obj.pos[0]+obj.width and pygame.mouse.get_pos()[1]-main_camera.y <= obj.pos[1]+obj.height
        ):
            return True
        else:
            return False
        
    def del_obj(self):
        self.find_curr_room()
        for obj in map_objs[main_camera.room_key]['objs']:
            if self.over_obj(obj):     
                map_objs[main_camera.room_key]['objs'].remove(obj)
        for spike in self.curr_room.spikes:
            if self.over_obj(spike):
                map_objs[main_camera.room_key]['spikes'].remove(spike)
        for loader in self.curr_room.loaders:
            if self.over_obj(loader):
                map_objs[main_camera.room_key]['loaders'].remove(loader)
        main_camera.curr_room.update_room_objs()
        self.save_map()

map_maker = Map_maker()  

def map_objs_to_json():
    dict_copy = {}
    for key in map_objs:
        dict_copy.setdefault(key,{})

        room = {'size':map_objs[key]['room'].size,'pos':str_to_tuple(key)}
        dict_copy[key].setdefault('room',room)

        objs = []
        for obj in map_objs[key]['objs']:
            objs.append({'pos':obj.pos,'size':obj.size,'texture_name':'Green.webp'})
        dict_copy[key].setdefault('objs',objs)

        spikes = []
        for spike in map_objs[key]['spikes']:
            spikes.append({'pos':spike.pos,'size':spike.size,'texture_name':'crowbox.png'})
        dict_copy[key].setdefault('spikes',spikes)

        loaders = []
        for loader in map_objs[key]['loaders']:
            loaders.append({'pos':loader.pos,'size':loader.size,'room_size':loader.room.size,
                            'room_pos':loader.room.pos,'texture_name':'Green.webp'})
        dict_copy[key].setdefault('loaders',loaders)
    return(dict_copy)