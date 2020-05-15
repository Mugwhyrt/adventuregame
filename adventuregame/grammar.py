"""
GRAMMAR

Methods and constants for translating and parsing text. Constants are intended
to cover non-game specific words such as verbs and prepositions. More game
specific nouns and the result of a parsed sentence will be passed from props
in the game

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
# Noun Dictionary
# dictionary for each noun for some action
nouns_dict = {"north" : ["north"],
              "south" : ["south"],
              "east" : ["east"],
              "west" : ["west"],
              "target" : ["target"],
              "enemy" : ["enemy", "foe", "villain", "monster"]}

# Preposition Dictionary
prepositions_dict = {"with" : ["with", "using"],
                "under" : ["under", "below", "beneath"],
                "above" : ["above", "over"],
                "in" : ["in", "among", "amongst", "within", "inside",
                        "amidst", "around"]}
# Articles Array
articles = ["the", "a", "an", "ye", "thee", "yon"]

# Word Table
# {"action sentence" : }
actionTable = {"baseTable" : [["verb", "direct object", "preposition", "indirect object"], None],
             "go north" : [["go", "north", "preposition", "indirect object"], actions.MoveNorth],
               "go east" : [["go", "east", "preposition", "indirect object"], actions.MoveEast],
               "go west" : [["go", "west", "preposition", "indirect object"], actions.MoveWest],
               "look inventory" : [["look", "inventory", "preposition", "indirect object"], actions.ViewInventory],
               "heal self" : [["heal", "direct object", "preposition", "indirect object"], actions.Heal],
               "search target" : [["search", "target", "preposition", "indirect object"], actions.Search],
               "attack enemy" : [["attack", "enemy", "preposition", "indirect object"],actions.Attack],
               "flee enemy" : [["flee", "enemy", "preposition", "indirect object"],actions.Flee]}

# Parser Method
# Receives user input (String) and lists of available actions and nouns
# Returns wordTable, [string, string, string, string], an array corresponding
#   to the ["verb", "direct object", "preposition", "indirect object"] for some action
#
# Parse is meant for 

def parser(userInput, actions, targets):
    # Word Table contains keys to inform the game
    # which action should be taken
    wordTable = actionTable["baseTable"][0].copy()
    # set string to lowercase and split by white space
    parsedString = userInput.lower().split()
    # search for and remove any articles
    i = 0
    while i < len(parsedString):
        if parsedString[i] in articles:
            parsedString.pop(i)
        i += 1
        
    # for each word in the string
    for i in range(len(parsedString)):
        word = parsedString[i]
        # for each key in verbs_dict
        for v in verbs_dict:
            # if key is in available actions
            # and word is in verbs_dict
            if v in actions and word in verbs_dict[v]:
                print("{} is in actions, and {} is in verbs_dict[{}]".format(v, word, v))
                wordTable[0] = v
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
        
        # for each key in nouns_dict
        for n in nouns_dict:
            # if key is in available nouns
            # and word is in nouns_dict
            if n in targets and word in nouns_dict[n] and word != wordTable[3]:
                # then it is the direct noun
                wordTable[1] = word
                continue
    return wordTable

# Translator Method
# Receives user input (string) and list of arbitrary nouns with their acceptable substitute
# Ex: if wordTranslations = {"enemy" : ["witch", "ogre"]} then "attack witch" would become "attack enemy"
# Returns a string with the subbed words
#
# Translator is for instances where there are context specific nouns that are equivalent to some
# existing term in a wordTable from actionTable. Translator simply substitutes words, it does
# not return a formatted word table

def translator(userInput, wordTranslations):
    # for each key in wordTranslations
    for t in wordTranslations:
        # for each element in translations array
        for w in wordTranslations[t]:
            userInput = userInput.replace(w, t)
    return userInput


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
    
