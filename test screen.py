import pygame
pygame.init()
screen = pygame.display.set_mode((1600,900),vsync=1)

font = pygame.font.SysFont("Arial",300)
def draw_text(text,font,color,pos):
    img = font.render(text, True, color)
    screen.blit(img,pos)
print(pygame.font.get_fonts()  )  
surface = pygame.transform.scale(pygame.image.load('Green.webp'),(1400,700))
surface2 = pygame.transform.scale(pygame.image.load('boxplayer.webp'),(300,300))
x,y = 0,0
clock = pygame.time.Clock()
dt = clock.tick(1000)/1000
while True:
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] == True: #and if vel < a vel and if on ground
        y -=100 *dt
    elif keys_pressed[pygame.K_s] == True: # increase max accel down
        y +=100 *dt


    #movement y
    if keys_pressed[pygame.K_a] == True: #
        x-= 100 * dt
    elif keys_pressed[pygame.K_d] == True:
        x += 100* dt
    screen.fill((255,255,255))
    surface.blit(surface2,(1200,0))
    screen.blit(surface,(x,y))
    print(x,y)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip() 
    