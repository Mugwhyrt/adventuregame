#import tiles
from props import MapTile, Enemy, Item
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
            _world[(x, y)] = None if tile_name == '' else tileSet[tile_name].copy()
            if _world[(x, y) ] != None:
                    _world[(x, y)].x = x
                    _world[(x, y)].y = y
    return [x_max, len(rows)]

def load_props():
    enemySet = Enemy.readFromTSV("resources/enemies.txt")
    itemSet = Item.readFromTSV("resources/items.txt")
    """Parses a file that describes the props in the _world object"""
    with open('resources/stage_1_prop.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
                prop_arr = cols[x].replace('\n', '').split(',')
                if prop_arr[0] != '':
                        for prop in prop_arr:
                                enemy = enemySet[prop].copy()
                                #enemy.addChild(itemSet["coin"].copy())
                                _world[(x, y)].addChild(enemy)
                        
