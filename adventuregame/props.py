"""
Props

A super class to define general behavior for any object that interacts with
the player. Props have
"""
#import actions, world

class Prop():
    def __init__(self, title, synonyms, actions, description, children):
        # single word title used to define as object in word table
        self.title = title
        # array of synonyms for prop's title
        self.synonyms = synonyms
        # array of word table verbs applicable to the prop
        self.actions = actions
        # string description of object
        self.description = description
        # array of prop children
        self.children = children

    def __str__(self):
        return self.description

    def getChildActions(self):
        childActions = {}
        for c in children:
            childActions.update(c.actions)
        return childActions

    def getChildTargets(self):
        childTargets = {}
        for c in children:
            childTargets[c.title] = c.nouns
        return childTargets

    def readFromCSV(self, fileName):
        raise NotImplementedError()

    def available_actions(self):
        raise NotImplementedError()

    
"""
Tiles

class for map tiles, map tile can contain any kind of prop.
"""

class MapTile(Prop):
    def __init__(self, title, synonyms, actions,
                 description, children, x, y):
        self.x = x
        self.y = y
        super().__init__(self, title, synonyms, actions,
                         description, children)

    def readFromCSV(fileName):
        tiles = {}
        with open(fileName, 'r') as f:
            rows = f.readlines()
        title = ""
        synonyms = []
        actions = []
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
            elif param == "actions":
                i = 1
                while i < len(line):
                    actions.append(line[i].replace("\n", ""))
                    i += 1
            elif param == "description":
                description = line[1].replace("\n", "")
                tiles[title] = [synonyms.copy(), actions.copy(), description]
                synonyms = []
                actions = []
        return tiles

if __name__ == "__main__":
    tileSet = MapTile.readFromCSV("resources/tiles.csv")
    for key in tileSet:
        tile = MapTile(key, tileSet[key][0], tileSet[key][1],
                       tileSet[key][2], [], 0, 1)
        print(tile)
    
