"""
GRAMMAR

Methods for translating and parsing text.
General approach is inspired by a talk by Evan Wright for KansasFest 2017
'Making a Text Adventure Parser' - https://www.youtube.com/watch?v=II3O1CJA-x8
"""
__author__ = "Zachary Rohman"

import actions
import vocabulary as vcb

# Word Table
# {"action sentence" : }
actionTable = {"baseTable" : [["verb", "direct object", "preposition", "indirect object"], None],
             "go north" : [["go", "north", "preposition", "indirect object"], actions.MoveNorth],
               "go east" : [["go", "east", "preposition", "indirect object"], actions.MoveEast],
               "go west" : [["go", "west", "preposition", "indirect object"], actions.MoveWest],
               "go south" : [["go", "south", "preposition", "indirect object"], actions.MoveSouth],
               "look inventory" : [["look", "inventory", "preposition", "indirect object"], actions.ViewInventory],
               "heal" : [["heal", "direct object", "preposition", "indirect object"], actions.Heal],
               "search target" : [["search", "target", "preposition", "indirect object"], actions.Search],
               "attack enemy" : [["attack", "enemy", "preposition", "indirect object"],actions.Attack],
               "flee enemy" : [["flee", "enemy", "preposition", "indirect object"],actions.Flee],
               "buy" : [["buy", "direct object", "preposition", "indirect object"], actions.Buy]}

# Parser Method
# Receives user input (String) and lists of available actions and nouns
# Returns wordTable, [string, string, string, string], an array corresponding
#   to the ["verb", "direct object", "preposition", "indirect object"] for some action
#
# Parse is meant for 

def parser(userInput, moves, targets):

    # Word Table contains keys to inform the game
    # which action should be taken
    wordTable = actionTable["baseTable"][0].copy()

    # set string to lowercase and split by white space
    parsedString = userInput.lower().split()

    # search for and remove any articles
    i = 0
    while i < len(parsedString):
        if parsedString[i] in vcb.articles:
            parsedString.pop(i)
        i += 1
        
    # for each word in the string
    for i in range(len(parsedString)):
        word = parsedString[i]
        # for each key in verbs_dict
        if word in moves:
            wordTable[0] = word
            continue

        # for each key in nouns_dict
        if word in targets and word != wordTable[3]:
            # then it is the direct noun
            wordTable[1] = word
            continue
        """
        No actions require prepositions just yet
        So commenting out to simplify coding process
        
        # check for prepositions and indirect objects
        for p in prepositions:
            # if the word is a preposition
            # and the following word is in the list of acceptable targets
            if word in prepositions[p] and i+1 < len(parsedString) and parsedString[i+1] in targets:
                wordTable[2] = p
                wordTable[3] = parsedString[i+1]
                continue
                """
    return wordTable

# Translator Method
# Receives user input (string) and list of arbitrary nouns with their acceptable substitute
# Ex: if wordTranslations = {"enemy" : ["witch", "ogre"]} then "attack witch" would become "attack enemy"
# Returns a string with the subbed words
#
# Translator is for instances where there are context specific nouns that are equivalent to some
# existing term in a wordTable from actionTable. Translator simply substitutes words, it does
# not return a formatted word table

def translator(userInput, wordTranslations, verbs, nouns):

    userInput = stringReplace(userInput, wordTranslations)
    userInput = stringReplace(userInput, verbs)
    userInput = stringReplace(userInput, nouns)
    
    return userInput

# String Replace
# receives user input(string) and a hash table of keys with an array of synonyms.
# replaces any synonyms with the associated key

def stringReplace(userInput, keyTable):
    for key in keyTable:
        for s in keyTable[key]:
            userInput = userInput.replace(s, key)
    return userInput

# Get Table Elements
# Takes a dictionary of wordTables and returns an array of the unique
# elements for the specified index corresponding to "verb", "direct object",
# "preposition", or "indirect object"
def getTableElement(tableDictionary, index):
    elements = []
    for t in tableDictionary:
        arr = t.split()
        if len(arr) > index and arr[index] not in elements:
            elements.append(arr[index])
    return elements

if __name__ == "__main__":
    
    # Translate Strings Params
    words_t = {"enemy" : ["ogre", "witch"]}
    # Parse String Params
    verbs_p = ["attack",
               "go"]
    nouns_p = ["enemy",
               "north"]

    # Test Strings
    testStrings = ["attack ogre with the sword", "with sword attack that ogre",
                   "attack witch with sword", "with bow attack witch",
                   "with bow attack ye enemy", "head north with key", "with sword ogre attack"]
    for s in testStrings:
        unparsedString = s
        print("testing: " + unparsedString)
        # Translate String
        unparsedString = translator(unparsedString, words_t)
        print(unparsedString)
        # Parse String
        print(parser(unparsedString, verbs_p, nouns_p))
        print("\n===============\n")
    
