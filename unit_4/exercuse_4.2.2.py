def parse_ranges(ranges_string):
    ranges = (num.split('-') for num in ranges_string.split(','))
    numbers = (num for start, stop in ranges for num in range(int(start), int(stop) + 1))

    return numbers


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == '__main__':
    main()
