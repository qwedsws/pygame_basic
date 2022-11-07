import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #width,height
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render('My game', False, 'Black')
score_surface = test_font.render('SCORE', False, 'Black')


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800,300))
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
score_rect = score_surface.get_rect(center=(400,50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('collide')

    screen.blit(sky_surface,(0,0)) # 0,0 is top left of the surface. its like x,y axis
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface,(5,5))
    pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos())
    pygame.draw.rect(screen,'Pink',score_rect)
    pygame.draw.rect(screen,'Pink',score_rect,10)
    pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
    screen.blit(score_surface,score_rect)

    if snail_rect.x < -100:
        snail_rect.x = 800

    snail_rect.x -= 3
    screen.blit(snail_surface,snail_rect)
    #print(player_rect.left)
    screen.blit(player_surface,player_rect)

    #if player_rect.colliderect(snail_rect):
    #    snail_rect.x += 80

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
    #    print('collision')

    pygame.display.update()
    clock.tick(60) # 60FPS limits While loop