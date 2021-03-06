class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Knife(Weapon):
    def __init__(self, name, damage):
        super(Knife, self).__init__(name, damage)
        self.sharp = True
        self.durability = 10

    def attack(self):
        if self.sharp:
            self.durability -= 1
            if self.durability <= 0:
                self.sharp = False


class Handgun(Weapon):
    def __init__(self, name, damage):
        super(Handgun, self).__init__(name, damage)
        self.shoot = True
        self.durability = 20

    def attack(self):
        if self.shoot:
            self.durability -= 1
            if self.durability <= 0:
                self.shoot = False


class Bat(Weapon):
    def __init__(self, name, damage):
        super(Bat, self).__init__(name, damage)
        self.swing = True
        self.durability = 10

    def attack(self):
        if self.swing:
            self.durability -= 1
            if self.durability <= 0:
                self.swing = False


class KatanaSword(Weapon):
    def __init__(self, name, damage):
        super(KatanaSword, self).__init__(name, damage)
        self.swing = True


class ShotGun(Weapon):
    def __init__(self, name, damage):
        super(ShotGun, self).__init__(name, damage)
        self.shoot = True


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)
        self.Heal = True
        self.durability = 5

    def heal(self):
        if self.Heal:
            self.durability -= 1
            if self.durability <= 0:
                self.Heal = False


class Apple(Consumable):
    def __init__(self, name):
        super(Apple, self).__init__(name)
        self.eat = True
        self.durability = 6

    def eat(self):
        if self.eat:
            self.durability -= 1
            if self.durability <= 0:
                self.eat = False


class Drink(Consumable):
    def __init__(self, name):
        super(Drink, self).__init__(name)


class Gatorade(Drink):
    def __init__(self, name):
        super(Gatorade, self).__init__(name)
        self.durability = 6


class Soda(Drink):
    def __init__(self, name):
        super(Soda, self).__init__(name)
        self.durability = 6


class AppleJuice(Drink):
    def __init__(self, name):
        super(AppleJuice, self).__init__(name)
        self.durability = 6


class Water(Drink):
    def __init__(self, name):
        super(Water, self).__init__(name)
        self.durability = 6


class Pizza(Consumable):
    def __init__(self, name):
        super(Pizza, self).__init__(name)
        self.durability = 4
        self.eat = True

    def eat(self):
        if self.eat:
            self.durability -= 1
            if self.durability <= 0:
                self.eat = False


class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
    print("You Turn The Key and The Engine Start's")


class Viper(Car):
    def __init__(self):
        super(Viper, self).__init__("Viper")


class Lamborghini(Car):
    def __init__(self):
        super(Lamborghini, self).__init__("Lamborghini")


class Van(Car):
    def __init__(self):
        super(Van, self).__init__("Van")


class AudiR8(Car):
    def __init__(self):
        super(AudiR8, self).__init__("Audi R8")
