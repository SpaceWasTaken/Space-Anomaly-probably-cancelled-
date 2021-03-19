import pygame, sys, json, time
from load_images import * 
from player import *
from tiles import * 
from collisions import *
from enemy_ import * 
from projectiles_ import *

pygame.init() # initializes pygame 

WIDTH, HEIGHT = 700, 394

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('space anomaly [rebuild]')

clock = pygame.time.Clock()
FPS = 47
lt = time.time()

# variables
player_rect = pygame.Rect(125, 727, 16, 29)
cursor_rect = cursor.get_rect()
gravity = 0
scroll = [0, 0]
mouse_pos = 0


def __blit__():

    win.blit(space_bg, (0, 0))
    win.blit(space_map, (0 - scroll[0], 0 - scroll[1]))

    tiles.tile_surf.fill((255, 255, 255))
    tiles.tile_surf.set_colorkey((255, 255, 255))
    tiles.create_chunks()
    win.blit(tiles.tile_surf, (0, 0))

    projectiles.move_projectile(win, scroll, player_rect.x,  player_rect.y)
    enemy.move_enemy()
    
    #-------------------------------# cursor related stuff
    pygame.mouse.set_visible(False) # erasing the cursor
    cursor_rect.center = pygame.mouse.get_pos()
    win.blit(cursor, (cursor_rect.x, cursor_rect.y))

    #-------------------------------# updating the display
    pygame.display.update()

# mainloop
running = True 
player = main_player()
tiles = tile()
projectiles = projectile(0,0)
enemy = enemies(200, 680)

while running:

    clock.tick(FPS)
    win.fill((0, 0, 0))
    
    dt = time.time() - lt
    lt = time.time()
    dt *= 47
    
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            running = False 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            projectiles.update(mouse_pos, scroll, player_rect.x, player_rect.y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.right = True
                player.idle = False
            if event.key == pygame.K_a:
                player.left = True
                player.idle = False
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                player.right = False
                player.left = False
                player.idle = True

    scroll[0] += (player_rect.x - scroll[0] - 334)*dt
    scroll[1] += (player_rect.y - scroll[1] - 168)*dt
        
    player_vel = [0,0]

    if player.right:
        player_vel[0] += 7*dt
    elif player.left:
        player_vel[0] += -7*dt

    #-------------------------------# pritoratizing the camera movement
    if player_rect.x < 336:
        scroll[0] = 0
    elif player_rect.x > 486:
        scroll[0] = 167

    if player_rect.y < 170:
        scroll[1] = 0
    elif player_rect.y > 630:
        scroll[1] = 472
    #-------------------------------#

    player_vel[1] += gravity*dt
    gravity += 1
    if gravity > 6:
        gravity = 6

    if key[pygame.K_SPACE] and collisions['bottom']:
        gravity = -15

    player_rect, collisions = collision_movement(player_rect, player_vel, tiles.rect_tiles)

    if collisions['bottom']:
        gravity = 0


    __blit__()

pygame.quit()

