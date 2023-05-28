def four_dividers(number):
    def is_divisible_by_four(x):
        return x % 4 == 0

    return list(filter(is_divisible_by_four, range(1, number + 1)))


def main():
    print(four_dividers(9))


if __name__ == '__main__':
    main()
