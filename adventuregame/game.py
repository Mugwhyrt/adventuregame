"""
Text Based Adventure Game
Adapted from a tutorial by Phillip Johnson

Original Description from Phillip Johnson:
A simple text adventure designed as a learning experience for new programmers.
__author__ = 'Phillip Johnson'
"""

import world, os, grammar
import vocabulary as vcb
from player import Player
import colorama
from colorama import Fore, Back


def play():
    """
    initialise map
    """
    colorama.init()
    scale = world.load_tiles()
    world.load_props()
    player = Player()
    # initialize an empty world map to the scale returned from loading
    # the world tiles
    player.worldMap = [[' X ' for x in range(scale[0])] for y in range(scale[1])]
    room = world.tile_exists(player.location_x, player.location_y)
    player.updateMap(room)
    print(Fore.WHITE, end  = '\r')
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        """
        get current tile at user's location
        """
        room = world.tile_exists(player.location_x, player.location_y)
        player.updateMap(room)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            """
            get available actions and user input
            """
            print(Fore.RED + Back.WHITE + "What do you do?")
            # room.available_actions() is {sentence key : [table, action()]}
            available_actions = room.available_actions()
            print(Fore.GREEN + Back.BLACK, end = '\r')
            #for action in available_actions:
            #    print(action)
            print(Fore.RED, end = '\r')
            # get user input
            user_input = input('Action: ')

            """
            process user input
            """
            # translate user input
            translated_input = grammar.translator(user_input, {},
                                                  vcb.verbs_dict,
                                                  vcb.nouns_dict)
            # parse user input
            actions = grammar.getTableElement(available_actions, 0)
            targets = grammar.getTableElement(available_actions, 1)
            action_input = grammar.parser(translated_input, actions, targets)
            #print("avail_actions: " + str(available_actions))
            #print("actions: " + str(actions))
            #print("targets: " + str(targets))
            #print("Action_Input: " + str(action_input))
            print(Fore.WHITE, end  = '\r')
            os.system("cls")

            """
            performed desired user action if allowed
            """
            for action in available_actions:
                # if action_input == action.key
                if action_input == available_actions[action][0]:
                    # player.do_action(action.action)
                    player.do_action(available_actions[action][1],
                                     **available_actions[action][1].kwargs)
                    break
    if not player.is_alive():
        print("You have died!")


if __name__ == "__main__":
    try:
        play()
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        print("Press Enter to continue ...")
        input()
