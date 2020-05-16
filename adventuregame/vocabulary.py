"""
VOCABULARY

Variables for translating and parsing text.

Variables are intended to cover non-game specific words such as verbs and
prepositions. More game specific nouns and the result of a parsed sentence
will be passed from props in the game

"""

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
                  "dine", "bite", "chew", "snack", "sup",
                  "feast", "gulp", "slup", "guzzle", "quaff", "gargle"],
         "heal" : ["heal"]}

# Noun Dictionary
# dictionary for each noun for some action
nouns_dict = {"north" : ["north"],
              "south" : ["south"],
              "east" : ["east"],
              "west" : ["west"],
              "target" : ["target"],
              "enemy" : ["enemy", "foe", "villain", "monster"],
              "inventory" : ["inventory", "stuff"]}

# Preposition Dictionary
prepositions_dict = {"with" : ["with", "using"],
                "under" : ["under", "below", "beneath"],
                "above" : ["above", "over"],
                "in" : ["in", "among", "amongst", "within", "inside",
                        "amidst", "around"]}
# Articles Array
articles = ["the", "a", "an", "ye", "thee", "yon"]
