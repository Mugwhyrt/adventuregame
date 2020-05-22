"""
Props

A super class to define general behavior for any object that interacts with
the player.
"""
__author__ = "Zach R"
import world, grammar, copy 

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
        # map of prop children
        self.children = children

    def __str__(self):
        return self.description

    def copy(self):
        return copy.copy(self)

    # Return a dictionary of the moves for each immediate child 
    def getChildMoves(self):
        childMoves = {}
        for c in children:
            childMoves.update(c.moves)
        return childMoves

    # Return a dictinory of the title and synonyms
    # for each immediate child
    def getChildTargets(self):
        childTargets = {}
        for c in children:
            childTargets[c.title] = c.nouns
        return childTargets

    # Add a child to the prop
    def addChild(self, child):
        if child.title not in self.children:
            self.children[child.title] = []
        self.children[child.title].append(child)

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

        tileSet = {}
        for key in tiles:
            tile = MapTile(key, tiles[key][0], {}, tiles[key][1],
                           {}, -1, -1)
            tileSet[key] = tile
        return tileSet
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        #moves = {}
        adjacent_moves_text = "\nThere are paths to the:\n"
        # TO DO
        # compress into for loop
        #   coords = [(xPlus_0, yPlus_0), etc]
        #   cardinals = ["east", "west", "north", "south"]
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
    
    def available_actions(self):
        """Returns all of the available actions in this room."""
        noEnemies = True
        availMoves = {}
        # iterate over children
        for c in self.children:
            if isinstance(self.children[c][0], Enemy):
                for e in self.children[c]:
                    self.description += "\nThere is a {}".format(e.title)
                    noEnemies = False
                    availMoves.update(e.moves)
                    # TO DO
                    # flee can be done once as soon as at least one enemy is detected
                    #availMoves["flee "+e.title][0] = availMoves["flee "+e.title][1](tile = self)
        if not self.pathsChecked:
            self.adjacent_moves()
        # actions need their function calls specified
        for m in self.moves:
            # if method is callable
            # it still needs it's function call specified
            if callable(self.moves[m][1]):
                self.moves[m][1] = self.moves[m][1]()
        if noEnemies:
            availMoves.update(self.moves)
        return availMoves

    def modify_player(self, the_player):
        pass

    def intro_text(self):
        self.available_actions()
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
        moves = moves
        attackString = "attack {}".format(title)
        fleeString = "flee {}".format(title)
        moves[attackString] = grammar.actionTable["attack enemy"].copy()
        moves[attackString][0][1] = title
        moves[attackString][1] = moves[attackString][1](enemy = self)
        moves[fleeString] = grammar.actionTable["flee enemy"].copy()
        moves[fleeString][0][1] = title
        super().__init__(title, synonyms, moves,
                         description, children)
    
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
            elif param == "description":
                description = line[1].replace("\n", "")
            elif param == "hp":
                hp = line[1].replace("\n", "")
            elif param == "damage":      
                damage = line[1].replace("\n", "")
                enemies[title] = [synonyms.copy(), description,
                                hp, damage]
                synonyms = []
                moves = []
                
        enemySet = {}
        for key in enemies:
            enemy = Enemy(key, enemies[key][0], {},
                           enemies[key][1], {}, int(enemies[key][2]),
                          int(enemies[key][3]))
            enemySet[key] = enemy
            
        return enemySet
    
if __name__ == "__main__":
    enemySet = Enemy.readFromTSV("resources/enemies.txt")
    tileSet = MapTile.readFromTSV("resources/tiles.txt")

    tileSet["CavePath_0"].addChild(enemySet["rat"].copy())
    tileSet["CavePath_0"].addChild(enemySet["ogre"].copy())
    actions = tileSet["CavePath_0"].available_actions()
    for a in actions:
        print(a)
    
