import pygame, math 

class projectile:
    def __init__(self, dist_x, dist_y):
        self.dist_x = dist_x
        self.dist_y = dist_y
        self.vel = 6
    def update(self, mouse, scroll, player_x, player_y):
        self.dist_x = mouse[0] - player_x
        self.dist_y = mouse[1] - player_y

    def move_projectile(self, surface, scroll, player_x, player_y):
        distance = math.atan2(self.dist_y, self.dist_x)
        player_x += math.cos(distance) * self.vel
        player_y += math.sin(distance) * self.vel

        pygame.draw.polygon(surface, ((255, 255, 255)), [(((player_x + 10) - scroll[0]), (player_y - scroll[1])), (((player_x + 7) - scroll[0]), ((player_y + 3) - scroll[1])), (((player_x + 10) - scroll[0]), ((player_y + 13) - scroll[1])), (((player_x + 13) - scroll[0]), ((player_y + 3) - scroll[1]))])


