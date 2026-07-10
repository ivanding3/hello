import pygame
import vars

pygame.init()


def draw_text(text,size,color,pos,dest):
    surface = pygame.font.SysFont("geistpixelregular",size).render(text, True, color)
    dest.blit(surface,pos)

esc_menu = False

def max(a,b,max=0):
    n = a-b
    if n<max:return max
    return n

class button:
    def __init__(self,pos,font_size,color,text,margin = 10):
        self.pos = pos
        self.font_size = font_size
        self.color = color
        self.text = text
        self.margin = margin
        self.width = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[0]+self.margin*2
        self.height = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[1]+self.margin*2



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
        if self.over_button == True:    
            if pygame.mouse.get_pressed()[0] == True:
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.pressed = False

            

                    

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
        self.over_button_detect()
        self.pressed_detect()
        self.display(dest)



#resume_button 
#settings_button
#controls_button 

    
  
        
       
    
def menu():
    pass

test_button = button((0,0),30,(0,255,0),"hello world")


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