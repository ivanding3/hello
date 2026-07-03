import pygame
pygame.init()
screen = pygame.display.set_mode((1600,900),vsync=1)

font = pygame.font.SysFont("Arial",300)
def draw_text(text,font,color,pos):
    img = font.render(text, True, color)
    screen.blit(img,pos)
print(pygame.font.get_fonts()  )  
while True:
    screen.fill((255,255,255))

    draw_text("hello world",font,(00,00,00),(0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip() 
    