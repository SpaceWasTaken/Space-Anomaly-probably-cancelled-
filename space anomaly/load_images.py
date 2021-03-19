# loading images
import pygame 

WIDTH, HEIGHT = 700, 394
pygame.display.set_mode((WIDTH, HEIGHT))


space_bg = pygame.image.load('space anomaly background.png').convert()

dirt = pygame.image.load('dirt.png').convert()
grass = pygame.image.load('grass.png').convert()

space_map = pygame.image.load('space map.png').convert()
space_map.set_colorkey((255, 255, 255))

walk_right = [pygame.image.load('walk right 1.png').convert(), pygame.image.load('walk right 2.png').convert(), pygame.image.load('walk right 3.png').convert()]
walk_right[0].set_colorkey((255, 255, 255))
walk_right[1].set_colorkey((255, 255, 255))
walk_right[2].set_colorkey((255, 255, 255))

walk_left = [pygame.image.load('walk left 1.png').convert(), pygame.image.load('walk left 2.png').convert(), pygame.image.load('walk left 3.png').convert()]
walk_left[0].set_colorkey((255, 255, 255))
walk_left[1].set_colorkey((255, 255, 255))
walk_left[2].set_colorkey((255, 255, 255))

bot_1 = pygame.transform.scale2x(pygame.image.load('enemy bot.png')).convert()
bot_1.set_colorkey((255, 255, 255))

cursor = pygame.image.load('cursor.png').convert()
cursor.set_colorkey((255, 255, 255))



