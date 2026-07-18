import pygame
import vars
import map_stuff
pygame.init()

buttons = []
def draw_text(text,size,color,pos,dest):
    surface = pygame.font.SysFont("geistpixelregular",size).render(text, True, color)
    dest.blit(surface,pos)

esc_menu = False

def max(a,b,max=0):
    n = a-b
    if n<max:return max
    return n

class button:
    def __init__(self,pos,font_size,color,text,margin = 10,toggleable = False,always_vis = True):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.font_size = font_size
        self.color = color
        self.text = text
        self.margin = margin
        self.width = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[0]+self.margin*2
        self.height = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[1]+self.margin*2
        self.size = (self.width,self.height)
        self.toggleable = toggleable
        self.pressed = False
        if always_vis:buttons.append(self)
    def locked(self):
        self.locked = False

        

    def over_button(self):
        self.over_button = False
    
    def over_button_detect(self):

        if (
        pygame.mouse.get_pos()[0] >= self.pos[0] and pygame.mouse.get_pos()[1] >= self.pos[1] and 
        pygame.mouse.get_pos()[0] <= self.pos[0]+self.width and pygame.mouse.get_pos()[1] <= self.height
        ):
            self.over_button = True

        else:
            self.over_button = False

    def pressed(self):
        self.pressed = False
    
    def pressed_detect(self):
        if not self.toggleable:
            if self.over_button == True:    
                if pygame.mouse.get_pressed()[0] == True:
                    self.pressed = True
                else:
                    self.pressed = False
            else:
                self.pressed = False
        else:
            if self.over_button == True:    
                if pygame.mouse.get_pressed()[0] and not self.locked:
                    self.pressed = not self.pressed
                    self.locked = True
                    

            

                    

    def display(self,dest):

        button_surface = pygame.transform.scale(pygame.Surface(self.pos),(self.width,self.height))
        if self.pressed == False:
            button_surface.fill(self.color)
        else:
            button_surface.fill((max(self.color[0],50),max(self.color[1],50),max(self.color[2],50))) 
        dest.blit(button_surface,self.pos)
      
        if self.over_button == False:
            draw_text(self.text,self.font_size,(0,0,0),(self.pos[0]+self.margin,self.pos[1]+self.margin),dest)
        else:
            draw_text(self.text,self.font_size,(80,80,80),(self.pos[0]+self.margin,self.pos[1]+self.margin),dest)

    def run_button(self,dest = vars.screen):
        if self.toggleable:
            if self.locked:
                if not pygame.mouse.get_pressed()[0]: self.locked = False
        self.over_button_detect()
        self.pressed_detect()
        self.display(dest)



#resume_button 
#settings_button
#controls_button 

    
  
        
       
    
def menu():
    pass


debug_button = button((1500,0),30,(255,0,0),"debug",toggleable=True)
map_mode_button = button((800,0),30,(0,0,255),'Map_mode',toggleable=True)
map_type_obj_b = button((map_mode_button.x +
                         map_mode_button.width,
                         map_mode_button.y),
                         30,
                         (128,0,0),
                         'obj',
                         toggleable=True,
                         always_vis=False)
map_type_obj_b.type = 'obj'

map_type_spike_b = button((map_mode_button.x +
                           map_mode_button.width +
                           map_type_obj_b.width,
                           map_mode_button.y),
                           30,
                           (128,0,0),
                           'spike',
                           toggleable=True,
                           always_vis=False)
map_type_spike_b.type = 'spike'

map_type_loader_b = button((map_mode_button.x +
                            map_mode_button.width +
                            map_type_obj_b.width +
                            map_type_spike_b.width,
                            map_mode_button.y),
                            30,
                            (128,0,0),
                            'loader',
                            toggleable=True,
                            always_vis=False)
map_type_loader_b.type = 'loader'

map_subbuttons = [map_type_obj_b,map_type_spike_b,map_type_loader_b]
def run_map_subbuttons():
    map_type_obj_b.run_button()    
    map_type_spike_b.run_button()  
    map_type_loader_b.run_button()  

    if map_type_obj_b.pressed:   
        if (map_type_obj_b.over_button and
            pygame.mouse.get_pressed()[0]):    
                map_type_spike_b.pressed = False
                map_type_loader_b.pressed = False
        map_stuff.map_maker.obj_type = 'obj'

    if map_type_spike_b.pressed:  
        if (map_type_spike_b.over_button and
            pygame.mouse.get_pressed()[0]):    
                map_type_obj_b.pressed = False
                map_type_loader_b.pressed = False    
        map_stuff.map_maker.obj_type = 'spike'  
    if map_type_loader_b.pressed:     
        if (map_type_loader_b.over_button and
            pygame.mouse.get_pressed()[0]):    
                map_type_spike_b.pressed = False
                map_type_obj_b.pressed = False    
        map_stuff.map_maker.obj_type = 'loader'  
if __name__ == '__main__':
    test_button = button((0,0),30,(0,255,0),"hello world")
    while True:
        vars.screen.fill((255,255,255))
        test_button.run_button()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.K_ESCAPE:
                esc_menu = True
        pygame.display.flip() 