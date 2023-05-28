class BigThing:
    def __init__(self, variable):
        self.variable = variable

    def size(self):
        if isinstance(self.variable, (int, float)):
            return self.variable
        elif isinstance(self.variable, (list, dict, str)):
            return len(self.variable)


class BigCat(BigThing):
    def __init__(self, variable, weight):
        super().__init__(variable)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "OK"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
