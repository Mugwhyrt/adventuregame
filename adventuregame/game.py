"""
A simple text adventure designed as a learning experience for new programmers.
"""
__author__ = 'Phillip Johnson'
import world
from player import Player
import colorama
from colorama import Fore, Back

def play():
    colorama.init()
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print(Fore.WHITE, end  = '\r')
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print(Fore.RED + Back.WHITE + "Choose an action")
            available_actions = room.available_actions()
            print(Fore.GREEN + Back.BLACK, end = '\r')
            for action in available_actions:
                print(action)
            print(Fore.RED, end = '\r')
            action_input = input('Action: ')
            print(Fore.WHITE, end  = '\r')
            os.system("cls")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    if not player.is_alive():
        print("You have died!")


if __name__ == "__main__":
    play()
