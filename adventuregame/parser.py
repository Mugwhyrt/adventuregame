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
verbs = {"go" : ["go", "head", "move", "walk", "run", "travel", "leave",
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
                  "feast", "gulp", "slup", "guzzle", "quaff", "gargle"]}
# Preposition Dictionary
prepositions = {"with" : ["with", "using"],
                "under" : ["under", "below", "beneath"],
                "above" : ["above", "over"],
                "in" : ["in", "among", "amongst", "within", "inside",
                        "amidst", "around"]}
# Articles Array
articles = ["the", "a", "an", "ye", "thee", "yon"]

# Parser Method
# Receives user input (String) and lists of available actions and nouns
# Returns

def parser(userInput, actions, nouns):
    # Word Table contains keys to inform the game
    # which action should be taken
    wordTable = ["verb", "direct object", "preposition", "indirect object"]

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
            if v in actions and word in verbs[v]:
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

if __name__ == "__main__":
    actions = ["attack"]
    nouns = ["sword", "ogre", "enemy"]
    testStrings = ["attack ogre with the sword", "with sword attack that ogre",
                   "attack witch with sword", "with bow attack witch",
                   "with bow attack ye enemy" ]
    for s in testStrings:
        unparsedString = s
        print("testing: " + unparsedString)
        print(parser(unparsedString, actions, nouns))
    
