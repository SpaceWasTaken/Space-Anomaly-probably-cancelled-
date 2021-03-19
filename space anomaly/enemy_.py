 
from load_images import bot_1

class enemies:
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.width = bot_1.get_width()
        self.height = bot_1.get_height()
        self.vel = [0,0]

    def move_enemy(self):
        from main import player_rect, win, scroll

        if self.x < player_rect.x:
            self.vel[0] = 3
        elif self.x > player_rect.x + player_rect.width:
            self.vel[0] = -3
        else:
            self.vel[0] = 0

        if self.y < player_rect.y:
            self.vel[1] = 3
        elif self.y > player_rect.y + player_rect.height:
            self.vel[1] = -3
        else:
            self.vel[1] = 0

        self.x += self.vel[0]
        self.y += self.vel[1]

        win.blit(bot_1, (self.x - scroll[0], self.y - scroll[1]))

