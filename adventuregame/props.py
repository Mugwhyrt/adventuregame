"""
Props

A super class to define general behavior for any object that interacts with
the player. Props have
"""
import actions, world

class Prop():
    def __init__(self, title, synonyms, moves, description, children):
        # single word title used to define as object in word table
        self.title = title
        # array of synonyms for prop's title
        self.synonyms = synonyms
        # array of word table verbs applicable to the prop
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

    def readFromCSV(self, fileName):
        raise NotImplementedError()

    def available_moves(self):
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
        super().__init__(title, synonyms, moves,
                         description, children)

    def readFromCSV(fileName):
        tiles = {}
        with open(fileName, 'r') as f:
            rows = f.readlines()
        title = ""
        synonyms = []
        moves = []
        description = ""
        for r in rows:
            line = r.split(',')
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

    #def available_moves()

if __name__ == "__main__":
    tileSet = MapTile.readFromCSV("resources/tiles.csv")
    for key in tileSet:
        #print(tileSet[key])
        tile = MapTile(key, tileSet[key][0], tileSet[key][1],
                       tileSet[key][2], [], 0, 1)
        print("name: {}\nlocation: {},{}\nDescription:\n{}\n".format(tile.title,
                                                                   tile.x,
                                                                   tile.y,
                                                                   tile))
    
