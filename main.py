import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #width,height
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0)) # 0,0 is top left of the surface. its like x,y axis
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface,(5,5))

    pygame.display.update()
    clock.tick(60) # 60FPS limits While loop