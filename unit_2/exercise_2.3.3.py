class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 0
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


def main():
    octopus1 = Octopus("Riki")
    octopus2 = Octopus()
    print(octopus1.get_name())
    print(octopus2.get_name())
    octopus1.set_name("Oliver")
    print(octopus1.get_name())
    print(Octopus.count_animals)


if __name__ == '__main__':
    main()
