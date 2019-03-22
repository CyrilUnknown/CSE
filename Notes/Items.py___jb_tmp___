class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage

class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor


    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
            print("%s has %d health left" % (self.name, self.health))

        def attack(self, target):
            print("%s attacks %s for %d damage" %
                  (self.name, target.name, self.weapon.damage))
            target.take_damage(self.weapom.damage)


# Items
sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
TheBeast_armor = Armor("Armor of the Gods", 10000000000000000)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor, 2"))
TheBeast_armor = Character("TheBeast", 10000000000, canoe, TheBeast_armor)

orc.attack(wiebe)
