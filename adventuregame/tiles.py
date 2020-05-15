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
            # moves.append( { key : action} )
            # moves.append( { parser.actionTable["go north"][0] : parser.actionTable["go north"][1]() } )
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
        super().__init__(x, y, items.Dagger(), "It's a dagger!")

    def intro_text(self):
        text = """
        Another dirty part of the cave.
        """
        if self.item.available:
            text += "You notice something shiny in the corner."
        return text


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5), "It's 5 gold coins!")

    def intro_text(self):
        text = """
        Another room."""
        
        if self.item.available:
            text += " Something shines from under the dirt\n"
        return text
    
class RockSlideRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5), "It's 5 gold coins!")

    def intro_text(self):
        text = """
        A pile of rocks blocks the way, but with a bit of work
        you managed to clear enough out of the way to crawl through.
        """
        if self.item.available:
            text +="""
        Something shines from under the pile of remaining rocks
        """
        return text
    
class OldJailRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger(), "It's a dagger!")
    def intro_text(self):
        text = """
        An old jail cell littered with garbage.
        """
        
        if self.item.available:
            text += """
        Maybe there's something useful to be found.
        """
        return text

class CauldronRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword(), "It's a sword!")
    def intro_text(self):
        text = """
        A large cauldron sits at the center of the room.
        The pile of human bones and smell of rotting flesh
        tells you more than you want to know about the witch's
        dietary habits.
        """
        
        if self.item.available:
            text += """
        It looks like the loot of former adventurers is mixed in with the bones.
            """
                
        return text

class StoreRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Hardtack(), "It's a mostly not moldy piece of hardtack!")
    def intro_text(self):
        text = """
        It's a store room! Crates and barrels line the wall.
        Most seem too rotted and waterlogged to be worth checking.
        """
        if self.item.available:
            text += """
        But there is at least one barrel has managed to avoid complete ruin.
        """
        return text
    
class OgreTreasureRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(300), "It's a treasure chest filled with gold coins!")

    def intro_text(self):
        text = """
        It's a room fit for an ogre. A nest of animal skins makes 
        up one corner of the room. There is a distinctive ogre-ish musk
        that fills the air and you do all you can to hold back your lunch.
        """
        if self.item.available:
            text += """
        A large wooden chest sits in the other corner of the room
            """
        else:
            text += """
        A large, empty wooden chest sits in the other corner of the room
            """
        return text

"""

ENEMY ROOMS

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
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            moves.append(actions.Heal())
            return moves

class ShadowRoom(EnemyRoom):
    def __init__(self, x, y):
        self.firstEncounter = True
        super().__init__(x, y, enemies.Shadow())
        
    def intro_text(self):
        return """
        Strange shadows flicker on the wall from a lone torch.
        Before long you realize these are no ordinary shadows,
        they begin to attack!

        Good luck trying to hit a shadow!
        """

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

class BatRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bats())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
        A swarm of bats swoop down from the ceiling!
            """
        else:
            return """
        The corpses of adorable bats litter the floor.
            """

class WitchRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Witch())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
        You've stumbled onto the lair of a wicked witch.
        She doesn't seem too happy to see you
            """
        else:
            return """
        The witch lays dead in the corner.
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
        A dead ogre reminds you of your triumph. The smell reminds
        you of the time you fell in a latrine.
            """

class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!

        You have died!
        """

    def modify_player(self, player):
        player.hp = 0

"""

SHOP ROOMS

"""

class ShopRoom(MapTile):
    def __init__(self, x, y, inventory):
        self.inventory = inventory
        super().__init__(x, y)

    def modify_player(self, the_player):
        pass
    
    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Heal())
        if (len(self.inventory) > 0):
            moves.append(actions.Buy(inventory=self.inventory))
        return moves

class HermitRoom(ShopRoom):
    def __init__(self, x, y):
        super().__init__(x, y, [items.Key()])
        self.inventory[0].value = 300
    def intro_text(self):
        text= """
        A grizzled hermit rests in the corner.
        """
        if (len(self.inventory) > 0):
            text += """
        He tells you he has something that may help you
            """
        else:
            text += """
        He has nothing left to help you
            """
        return text

"""
LockedDoor

directions is an array containing chars indicating which directions
a player can move in while door is locked
"""
class LockedDoor(MapTile):
    def __init__(self, x, y, directions):
        self.locked = True
        self.directions = directions
        super().__init__(x, y)
        
    def modify_player(self, the_player):
        for i in range(len(the_player.inventory)):
            if type(the_player.inventory[i]).__name__ == "Key":
                del the_player.inventory[i]
                self.locked = False
                print("""
        You use a key to unlock the door
                """)
        if self.locked:
            print("""
        You have no key to unlock the door
            """)
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y) and ('e' in self.directions or not self.locked):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y) and ('w' in self.directions or not self.locked):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1) and ('n' in self.directions or not self.locked):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1) and ('s' in self.directions or not self.locked):
            moves.append(actions.MoveSouth())
        return moves
    def intro_text(self):
        text ="""
        You are able to pass through the unlocked door.
        """
        if self.locked:
            text ="""
        A locked door blocks your way.
            """
            
        return text

class LockedDoor_N(LockedDoor):
    def __init__(self, x, y):
        super().__init__(x, y, ['n'])
