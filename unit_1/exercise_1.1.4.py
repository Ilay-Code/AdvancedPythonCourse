import functools


def sum_of_digits(number):
    def add_digits(x, y):
        return int(x) + int(y)

    return functools.reduce(add_digits, str(number))


def main():
    print(sum_of_digits(981))


if __name__ == '__main__':
    main()
