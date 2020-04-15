"""Describes the tiles in the world space."""
__author__ = 'Phillip Johnson'

import items, enemies, actions, world


class MapTile:
    """The base class for a tile within the world space"""
    def __init__(self, x, y):
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Heal())
        
        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        text = """
        For days you have been travelling through the mountains, trying
        to find some passage to the otherside. All your equipment and
        food was lost trying to ford a river. All you have to defend
        yourself now is a rock, and you have no food to eat.

        Today however it seems that luck is with you, as you've
        finally found a passage leading into the side of the mountain.
        There are many miles to go should you try to travel around the
        mountains, you have no choice but to take your chances in the
        dark caverns.
        """
        return text

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        You have reached the other side of the mountains!
        """

    def modify_player(self, player):
        player.victory = True
"""

GENERIC ROOMS

"""
class EmptyCavePath_0(MapTile):
    def intro_text(self):
        return """
        The cave walls are damp and you hear a steady drip of water
        from the stalactites above.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass
class EmptyCavePath_1(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass
class EmptyCavePath_2(MapTile):
    def intro_text(self):
        return """
        The bones of previous explorers crunch and crack under your feet.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class Stalagmites(MapTile):
    def intro_text(self):
        return """
        A dense cluster of stalagmites lay ahead of you, there's just enough
        room to squeeze through.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class CoffinRoom(MapTile):
    def intro_text(self):
        return """
        A row of beat up coffins fill the room. Whatever was in
        them before was picked through long ago. There is a passage
        on the far side of the room.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass

"""

LOOT ROOMS

"""
class LootRoom(MapTile):
    """A room that adds something to the player's inventory"""
    def __init__(self, x, y, item, itemText):
        self.item = item
        self.itemText = itemText
        super().__init__(x, y)

    def modify_player(self, the_player):
        pass

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Heal())
        if self.item.available: 
            moves.append(actions.Search(item = self.item, text = self.itemText))
        return moves


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        Someone dropped a 5 gold piece. You pick it up.
        """


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An ogre is blocking your path!
            """
        else:
            return """
            A dead ogre reminds you of your triumph.
            """


class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!

        You have died!
        """

    def modify_player(self, player):
        player.hp = 0
