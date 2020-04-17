import random
import items, world

__author__ = 'Phillip Johnson'


class Player():
    def __init__(self):
        self.inventory = [items.Rock()]
        self.maxhp = 100
        self.hp = self.maxhp
        self.gold = 15
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

            def add_loot(self, item, text):
        print(text)
        item.available = False
        if(type(item).__name__ == "Gold"):
            self.gold += item.amt
        else:
            self.inventory.append(item)

    def buy(self, inventory):
        print("What would you like to buy?")
        for i in range(len(inventory)):
            item = inventory[i]
            print(str(i+1) +") " + item.name + ", cost: " + str(item.value) + " gold coins")
        print("You have " + str(self.gold) + " gold coins to spend.")
        waiting = True
        while waiting:
            choice = input("Enter the # item you would like buy, or 'e' to leave: ")
            if choice.isdigit() and int(choice)-1 in range(len(inventory)):
                item = inventory[int(choice)-1]
                if item.value <= self.gold:
                    self.gold -= item.value
                    self.inventory.append(item)
                    del inventory[int(choice)-1]
                else:
                    print("you don't have enough money for that!")
                waiting = False
            elif choice == 'e':
                waiting = False

    def heal(self):
        if self.hp < self.maxhp:
            print("What would you like to heal yourself with?")
            healingItems = False
            for i in range(len(self.inventory)):
                if isinstance(self.inventory[i], items.Healing):
                    healingItems = True
                    item = self.inventory[i]
                    print(str(i+1) + ") " + item.name + ", restores " + str(item.amt) + " hp")
            
            waiting = False
            if healingItems:
                waiting = True
            else:
                print("Whoops! You have nothing to heal yourself with.")
            while waiting:
                choice = input("enter the # item you would like to heal yourself with, or 'e' to return to previous menu: ")
                if choice.isdigit() and int(choice)-1 in range(len(self.inventory)):
                    if isinstance(self.inventory[int(choice)-1], items.Healing):
                        item = self.inventory[int(choice)-1]
                        if self.hp + item.amt > self.maxhp:
                            self.hp = self.maxhp
                        else:
                            self.hp += item.amt
                        print("Your health is now " + str(self.hp) + "/" + str(self.maxhp))
                        del self.inventory[int(choice)-1]
                        waiting = False
                    else:
                        print("You can't heal yourself with that item")
                elif choice == 'e':
                    waiting = False
        else:
            print("You're already at full health!")

