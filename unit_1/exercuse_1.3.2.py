import functools


def is_prime(number):
    return functools.reduce(lambda x, y: x and y, (number % i != 0 for i in range(2, number)), True) and number > 1


def main():
    print(is_prime(42))
    print(is_prime(43))


if __name__ == '__main__':
    main()
