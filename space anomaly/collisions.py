
def collisions(cube, tiles):
    collisions_list = []

    for tile in tiles:
        if cube.colliderect(tile):
            collisions_list.append(tile)
    return collisions_list

def collision_movement(cube, vel, tiles):
    collisions_directions = {
        'top' : False,
        'bottom' : False,
        'left' : False,
        'right' : False
    }

    cube.x += vel[0]
    collisions_list = collisions(cube, tiles)
    for tile in collisions_list:
        if vel[0] > 0:
            cube.right = tile.left
            collisions_directions['right'] = True
        elif vel[0] < 0:
            cube.left = tile.right
            collisions_directions['left'] = True

    cube.y += vel[1]
    collisions_list = collisions(cube, tiles)
    for tile in collisions_list:
        if vel[1] > 0:
            cube.bottom = tile.top
            collisions_directions['bottom'] = True
        elif vel[1] < 0:
            cube.top = tile.bottom
            collisions_directions['top'] = True
    return cube, collisions_directions



