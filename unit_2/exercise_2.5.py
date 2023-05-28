class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self.name = name
        self.hunger = hunger

    def get_name(self):
        return self.name

    def is_hungry(self):
        return self.hunger > 0

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("Meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear Lord!")

    _stink_count = 6


class Unicorn(Animal):
    def talk(self):
        print("Good morning, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

    _color = "Green"


def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky"),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    for animal in zoo_lst:
        print(animal.get_name(), animal.__class__.__name__)
        while animal.is_hungry():
            animal.feed()

    for animal in zoo_lst:
        animal.talk()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
