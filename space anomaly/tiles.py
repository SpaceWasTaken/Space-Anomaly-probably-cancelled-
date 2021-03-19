import json
import pygame 

# loading the tiles
def load_tiles(file):
    load_map = open(file + '.py', 'r')
    game_map_data = load_map.read()
    load_map.close()
    
    game_map = json.loads(game_map_data)

    return game_map
    
game_map = load_tiles('map1')


class tile:
    import load_images 

    def __init__(self):
        self.width = 33
        self.chunkx_no = 8
        self.chunky_no = 5
        self.chunk_size = 8
        self.tile_index = 1
        self.rect_tiles = []
        self.tile_surf = pygame.Surface((890, 890))
        self.tile_types = {
            1 : self.load_images.dirt,
            2 : self.load_images.grass
        }


    def create_chunks(self):
        from main import scroll

        for tile in game_map:
            self.rect_tiles.append(pygame.Rect(game_map[tile][0][0], game_map[tile][0][1], game_map[tile][1][0], game_map[tile][1][1]))
                #update_rects.append(pygame.Rect(game_map[tile][0][0] * self.width, game_map[tile][0][1] * self.width, self.width, self.width))
                
