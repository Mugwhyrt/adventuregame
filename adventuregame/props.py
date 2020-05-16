"""
Props

A super class to define general behavior for any object that interacts with
the player. Props have
"""
import actions, world

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
        

    
"""
Tiles

class for map tiles, map tile can contain any kind of prop.
"""

class MapTile(Prop):
    def __init__(self, nouns, actions, description, children, x, y):
