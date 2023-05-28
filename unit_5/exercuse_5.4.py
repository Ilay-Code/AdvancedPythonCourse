class IDIterator:
    """
    Iterator class for generating valid ID numbers.

    Attributes:
        id_ (int): The ID number to start generating from.

    Methods:
        __iter__(): Returns the iterator object.
        __next__(): Generates the next valid ID number.

    Raises:
        StopIteration: If the ID number reaches 999999999.

    """

    def __init__(self, id_):
        """
        Initializes an IDIterator object with the given ID number.

        Args:
            id_ (int): The ID number to start generating from.

        """
        self.id_ = id_

    def __iter__(self):
        """
        Returns the iterator object.

        Returns:
            IDIterator: The iterator object.

        """
        return self

    def __next__(self):
        """
        Generates the next valid ID number.

        Returns:
            int: The next valid ID number.

        Raises:
            StopIteration: If the ID number reaches 999999999.

        """
        if self.id_ >= 999999999:
            raise StopIteration
        self.id_ += 1
        while not check_id_valid(self.id_):
            self.id_ += 1
        return self.id_


def check_id_valid(id_number):
    """
    Checks the validity of an ID number.

    Args:
        id_number (int): The ID number to be checked.

    Returns:
        bool: True if the ID number is valid, False otherwise.

    """
    digits = [int(d) for d in str(id_number)]
    multiplied_digits = [digits[i] * (1 if i % 2 == 0 else 2) for i in range(len(digits))]
    summed_digits = [n % 10 + n // 10 if n >= 10 else n for n in multiplied_digits]
    total_sum = sum(summed_digits)
    return total_sum % 10 == 0


def id_generator(id_number):
    """
    Generator function for generating valid ID numbers.

    Args:
        id_number (int): The ID number to start generating from.

    Yields:
        int: The next valid ID number.

    """
    current_id = id_number
    while current_id < 999999999:
        current_id += 1
        while not check_id_valid(current_id):
            current_id += 1
        yield current_id


def main():
    user_id = int(input("Enter ID: "))
    generator_type = input("Generator or Iterator? (gen/it)? ")

    if generator_type == "gen":
        id_generator_obj = id_generator(user_id)
        for _ in range(10):
            next_id = next(id_generator_obj)
            print(next_id)
    elif generator_type == "it":
        id_iterator = IDIterator(user_id)
        for _ in range(10):
            next_id = next(id_iterator)
            print(next_id)
    else:
        print("Invalid input. Please enter 'gen' or 'it'.")


if __name__ == '__main__':
    main()