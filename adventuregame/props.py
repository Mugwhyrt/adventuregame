"""
Props

A super class to define general behavior for any object that interacts with
the player
"""

class Prop():
    def __init__(self, nouns, actions, description, children):
        self.nouns = nouns
        self.actions = actions
        self.description = description
        self.children = children

    def __str__(self):
        return self.description

    
