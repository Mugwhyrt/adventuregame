#import tiles
from props import MapTile
__author__ = 'Phillip Johnson'

_world = {}
starting_position = (0, 0)

def tile_exists(x, y):
        """Returns the tile at the given coordinates or None if there is no tile.

        :param x: the x-coordinate in the worldspace
        :param y: the y-coordinate in the worldspace
        :return: the tile at the given coordinates or None if there is no tile
        """
        return _world.get((x, y))


def load_tiles():
    tileSet = MapTile.readFromTSV("resources/tiles.txt")
    #for key in tileSet:
    #    tile = MapTile(key, tileSet[key][0], tileSet[key][1],
    #                   tileSet[key][2], [], 0, 1)
    """Parses a file that describes the world space into the _world object"""
    with open('resources/stage_1_map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else MapTile(tile_name,
                                                                  tileSet[tile_name][0],
                                                                  tileSet[tile_name][1],
                                                                  tileSet[tile_name][2],
                                                                  [], x, y)
    return [x_max, len(rows)] 
