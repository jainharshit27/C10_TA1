import pygame
#Import pymunk and pymunk.pygame_util

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Declare space and assign pymunk.Space()
#Declare draw_options and assign pymunk.pygame_util.DrawOptions(screen)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    
    #Reload space using space.step(1/60)
    
    clock.tick(60)
