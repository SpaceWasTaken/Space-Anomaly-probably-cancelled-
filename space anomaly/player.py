
class main_player:

    def __init__(self):
        self.animation_frames = 0
        self.right = False
        self.left = False 
        self.idle = True
        self.jump = False 

    def animate_frames(self, surface):
        import load_images
        from main import player_rect, scroll
        
        if self.animation_frames + 1 >= 9:
            self.animation_frames = 0

        if not self.idle:
            if self.right:
                surface.blit(load_images.walk_right[self.animation_frames // 3], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
                self.animation_frames += 1

            elif self.left:
                surface.blit(load_images.walk_left[self.animation_frames // 3], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
                self.animation_frames += 1

        if self.idle:
            surface.blit(load_images.walk_right[0], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
