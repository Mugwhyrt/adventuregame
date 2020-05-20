"""
Props

A super class to define general behavior for any object that interacts with
the player. Props have
"""
__author__ = "Zach R"
import world, grammar

class Prop():
    def __init__(self, title, synonyms, moves, description, children):
        # single word title used to define as object in word table
        self.title = title
        # array of synonyms for prop's title
        self.synonyms = synonyms
        # map of word table verbs applicable to the prop
        self.moves = moves
        # string description of object
        self.description = description
        # array of prop children
        self.children = children

    def __str__(self):
        return self.description

    def getChildMoves(self):
        childMoves = {}
        for c in children:
            childMoves.update(c.moves)
        return childMoves

    def getChildTargets(self):
        childTargets = {}
        for c in children:
            childTargets[c.title] = c.nouns
        return childTargets

    def readFromTSV(self, fileName):
        raise NotImplementedError()

    def available_actions(self):
        raise NotImplementedError()

    
"""
Tiles

class for map tiles, map tile can contain any kind of prop.
"""

class MapTile(Prop):
    def __init__(self, title, synonyms, moves,
                 description, children, x, y):
        self.x = x
        self.y = y
        self.pathsChecked = False
        moves = moves
        moves["look inventory"] = grammar.actionTable["look inventory"].copy()
        moves["heal"] = grammar.actionTable["heal"].copy()
        
        super().__init__(title, synonyms, moves,
                         description, children)

    def readFromTSV(fileName):
        tiles = {}
        with open(fileName, 'r') as f:
            rows = f.readlines()
        title = ""
        synonyms = []
        description = ""
        for r in rows:
            line = r.split('\t')
            param = line[0]
            if param == "title":
                    title = line[1].replace("\n", "")
            elif param == "synonyms":
                i = 1
                while i < len(line):
                    synonyms.append(line[i].replace("\n", ""))
                    i += 1
            elif param == "description":
                description = line[1].replace("\n", "")
                tiles[title] = [synonyms.copy(), description]
                synonyms = []
                
        return tiles
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        #moves = {}
        adjacent_moves_text = "\nThere are paths to the:\n"
        if world.tile_exists(self.x + 1, self.y):
            # moves.append( { key : action} )
            self.moves["go east"] = grammar.actionTable["go east"].copy()
            #moves.append(actions.MoveEast())
            adjacent_moves_text += " East "
        if world.tile_exists(self.x - 1, self.y):
            #moves.append(actions.MoveWest())
            self.moves["go west"] = grammar.actionTable["go west"].copy()
            adjacent_moves_text += " West "
        if world.tile_exists(self.x, self.y - 1):
            #moves.append(actions.MoveNorth())
            self.moves["go north"] = grammar.actionTable["go north"].copy()
            adjacent_moves_text += " North "
        if world.tile_exists(self.x, self.y + 1):
            #moves.append(actions.MoveSouth())
            self.moves["go south"] = grammar.actionTable["go south"].copy()
            adjacent_moves_text += " South "
        if not self.pathsChecked:
            self.description += adjacent_moves_text
            self.pathsChecked = True
        #return self.moves
    
    def available_actions(self):
        """Returns all of the available actions in this room."""
        if not self.pathsChecked:
            self.adjacent_moves()
        # actions need their function calls specified
        for m in self.moves:
            # if method is callable
            # it still needs it's function call specified
            if callable(self.moves[m][1]):
                self.moves[m][1] = self.moves[m][1]()
        return self.moves

    def modify_player(self, the_player):
        pass

    def intro_text(self):
        self.adjacent_moves()
        return self.description

"""
Enemies

enemies subclass
"""

class Enemy(Prop):
    def __init__(self, title, synonyms, moves, description,
                 children, hp, damage):
        self.hp = hp
        self.damage = damage
        super().__init__(title, synonyms,
                         ["attack {}".format(title), "flee {}".format(title)],
                         description, children, hp, damage)

    def is_alive(self):
        return self.hp > 0

    def readFromTSV(fileName):
        enemies = {}
        with open(fileName, 'r') as f:
            rows = f.readlines()
        title = ""
        synonyms = []
        moves = []
        description = ""
        for r in rows:
            line = r.split('\t')
            param = line[0]
            if param == "title":
                    title = line[1].replace("\n", "")
            elif param == "synonyms":
                i = 1
                while i < len(line):
                    synonyms.append(line[i].replace("\n", ""))
                    i += 1
            elif param == "moves":
                i = 1
                while i < len(line):
                    moves.append(line[i].replace("\n", ""))
                    i += 1
            elif param == "description":
                description = line[1].replace("\n", "")
                tiles[title] = [synonyms.copy(), moves.copy(), description]
                synonyms = []
                moves = []
        return tiles
    
if __name__ == "__main__":
    tileSet = MapTile.readFromTSV("resources/tiles.txt")
    for key in tileSet:
        tile = MapTile(key, tileSet[key][0], tileSet[key][1],
                       tileSet[key][2], [], 0, 1)
        print("name: {}\nlocation: {},{}\nDescription:\n{}\n".format(tile.title,
                                                                   tile.x,
                                                                   tile.y,
                                                                   tile))
    
