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

import actions


# Verb Dictionary
# dictionary for each action verb with a list of synonyms
verbs_dict = {"go" : ["go", "head", "move", "walk", "run", "travel", "leave",
                 "pass", "journey",  "depart", "advance", "exit"],
         "attack" : ["attack", "kill", "assault", "beat", "hit", "hurt",
                     "bash", "assail", "harm", "strike", "stab", "whop",
                     "wallop", "whack", "bop"],
         "use" : ["use", "equip", "employ", "wield", "manipulate",
                  "utilize", "adorn", "furnish", "arm"],
         "look" : ["look", "search", "inspect", "view", "peep",
                   "scrutinize", "survey", "observe", "review",
                   "probe", "investigate"],
         "buy" : ["buy", "purchase", "procure", "acquire", "obtain",
                  "take"],
         "steal" : ["steal",  "loot", "snatch", "pickpocket", "pilfer",
                    "pilfer", "swipe", "pinch", "poach", "shoplift"],
         "flee" : ["flee", "escape","decamp", "scram", "hightail", "bolt",
                   "disappear", "vamoose", "skedaddle", "scram"],
         "eat" : ["eat", "drink", "consume", "devour", "swallow",
                  "dine", "bite", "chew", "snack", "sup", "wolf",
                  "feast", "gulp", "slup", "guzzle", "quaff", "gargle"],
         "heal" : ["heal"]}

# Preposition Dictionary
prepositions_dict = {"with" : ["with", "using"],
                "under" : ["under", "below", "beneath"],
                "above" : ["above", "over"],
                "in" : ["in", "among", "amongst", "within", "inside",
                        "amidst", "around"]}
# Articles Array
articles_dict = ["the", "a", "an", "ye", "thee", "yon"]

# Word Table
# {"action sentence" : }
actionTable = {"baseTable" : [["verb", "direct object", "preposition", "indirect object"], None],
             "go north" : [["go", "north", "preposition", "indirect object"], actions.MoveNorth],
               "go east" : [["go", "east", "preposition", "indirect object"], actions.MoveEast],
               "go west" : [["go", "west", "preposition", "indirect object"], actions.MoveWest],
               "look inventory" : [["look", "inventory", "preposition", "indirect object"], actions.ViewInventory],
               "heal self" : [["heal", "self", "preposition", "indirect object"], actions.Heal],
               "search target" : [["search", "target", "preposition", "indirect object"], actions.Search],
               "flee enemy" : [["flee", "enemy", "preposition", "indirect object"],actions.Flee],
               "attack enemy" : [["attack", "enemy", "preposition", "indirect object"],actions.Attack]}

# Parser Method
# Receives user input (String) and lists of available actions and nouns
# Returns wordTable, [string, string, string, string], an array corresponding
#   to the ["verb", "direct object", "preposition", "indirect object"] for some action
#
# Parse is meant for 

def parser(userInput, verbs, nouns, prepositions):
    # Word Table contains keys to inform the game
    # which action should be taken
    wordTable = actionTable["baseTable"][0]
    # set string to lowercase and split by white space
    parsedString = userInput.lower().split()
    
    # search for and remove any articles
    i = 0
    while i < len(parsedString):
        if parsedString[i] in articles:
            parsedString.pop(i)
        i += 1
    for i in range(len(parsedString)):
        word = parsedString[i]
        # check for verbs
        for v in verbs:
            # if v is an 
            if v in verbs_dict and word in verbs[v]:
                wordTable[0] = v
                continue
        # check for prepositions and indirect objects
        for p in prepositions:
            if word in prepositions[p] and i+1 < len(parsedString) and parsedString[i+1] in nouns:
                wordTable[2] = p
                wordTable[3] = parsedString[i+1]
                continue
        # check for direct objects
        if word in nouns and word != wordTable[3]:
            wordTable[1] = word
            continue
        
    return wordTable

# Translator Method
# Receives user input (string) and list of arbitrary nouns with their acceptable substitute
# Ex: if acceptableNouns = ["witch", "ogre"] then "attack witch" would become "attack enemy"
# Returns a string with the subbed words
#
# Translator is for instances where there are context specific nouns that are equivalent to some
# existing term in a wordTable from actionTable. Translator simply substitute words, it does
# not return


if __name__ == "__main__":
    
    # Translate Strings Params
    #verbs_t
    # Parse String Params
    verbs_p = ["attack"]
    nouns_p = ["enemy"]
    prepositions_p = []

    # Test Strings
    testStrings = ["attack ogre with the sword", "with sword attack that ogre",
                   "attack witch with sword", "with bow attack witch",
                   "with bow attack ye enemy" ]
    for s in testStrings:
        unparsedString = s
        print("testing: " + unparsedString)
        # Translate String
        #print(translater(untranslatedString, verbs_t, nouns_t, 
        # Parse String
        print(parser(unparsedString, verbs_p, nouns_p, prepositions_p))
    
