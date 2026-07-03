import pygame
pygame.init()
screen = pygame.display.set_mode((1600,900),vsync=1)


def draw_text(text,size,color,pos):
    img = pygame.font.SysFont("geistpixelregular",size).render(text, True, color)
    screen.blit(img,pos)

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
    


    def over_button(self):
        self.over_button = False
    
    def over_button_detect(self):
        width = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[0]+self.margin*2
        height = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[1]+self.margin*2
        if (
        pygame.mouse.get_pos()[0] >= self.pos[0] and pygame.mouse.get_pos()[1] >= self.pos[1] and 
        pygame.mouse.get_pos()[0] <= self.pos[0]+width and pygame.mouse.get_pos()[1] <= height
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

            

                    

    def display(self):
        width = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[0]+self.margin*2
        height = pygame.font.SysFont("geistpixelregular",self.font_size).size(self.text)[1]+self.margin*2
        button_surface = pygame.transform.scale(pygame.Surface(self.pos),(width,height))
        if self.pressed == False:
            button_surface.fill(self.color)
        else:
            button_surface.fill((max(self.color[0],50),max(self.color[1],50),max(self.color[2],50))) 
        screen.blit(button_surface,self.pos)
      
        if self.over_button == False:
            draw_text(self.text,self.font_size,(0,0,0),(self.pos[0]+self.margin,self.pos[1]+self.margin))
        else:
            draw_text(self.text,self.font_size,(80,80,80),(self.pos[0]+self.margin,self.pos[1]+self.margin))
    def run_button(self):
        self.over_button_detect()
        self.pressed_detect()
        self.display()



#resume_button 
#settings_button
#controls_button 

    
  
        
       
    
def menu():
    pass

test_button = button((0,0),30,(0,255,0),"hello world")


if __name__ == '__main__':
    test_button = button((0,0),30,(0,255,0),"hello world")
    while True:
        screen.fill((255,255,255))
        test_button.run_button()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.K_ESCAPE:
                esc_menu = True
        pygame.display.flip() 