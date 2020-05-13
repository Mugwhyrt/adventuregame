"""
TEXT PARSER

Methods and constants for parsing text. Constants are intended to cover
non-game specific words such as verbs and prepositions. More game specific
nouns and the result of a parsed sentence will be handled within the
context of the game

General approach is inspired by a talk by Evan Wright for KansasFest 2017
'Making a Text Adventure Parser' - https://www.youtube.com/watch?v=II3O1CJA-x8
"""
__author__ = "Zachary Rohman"


# Verb Dictionary
verbs = {}
# Preposition Dictionary
prepositions = {}

# Parser Method
# Receives user input (String) and lists of available actions and nouns
# Returns

def parser():
    # Word Table contains keys to inform the game
    # which action should be taken
    wordTable = ["verb", "direct object", "preposition", "indirect object"]
    return wordTable
