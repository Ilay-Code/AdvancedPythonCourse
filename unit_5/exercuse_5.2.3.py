from itertools import combinations


def count_options():
    bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    options = []

    for b in range(1, len(bills) + 1):
        for combination in combinations(bills, b):
            if sum(combination) == 100:
                options.append(combination)

    unique_options = set(tuple(sorted(option)) for option in options)

    for option in unique_options:
        print(option)

    return len(unique_options)


def main():
    num_options = count_options()
    print("Number of options:", num_options)


if __name__ == '__main__':
    main()
