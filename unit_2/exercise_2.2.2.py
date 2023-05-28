class Octopus:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    octopus1 = Octopus("Octavio", 7)
    octopus2 = Octopus("Octavia", 3)
    octopus1.birthday()
    print(f"{octopus1.name} is {octopus1.get_age()} years old.")
    print(f"{octopus2.name} is {octopus2.get_age()} years old.")


if __name__ == '__main__':
    main()
