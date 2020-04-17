"""Describes the items in the game."""
__author__ = 'Phillip Johnson'


class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.available = True
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=1)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A dulled iron sword. Somewhat more dangerous than a dagger and much more dangerous than a rock!",
                         value=15,
                         damage=15)

class Healing(Item):
    def __init__(self, name, description, value, amt):
        self.amt = amt
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHeals: {} hp".format(self.name, self.description, self.value, self.amt)


class Hardtack(Healing):
    def __init__(self):
        super().__init__(name="Hardtack",
                        description="A rock hard piece of hardtack, don't chip a tooth!",
                        value=0,
                        amt=5)
        
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
