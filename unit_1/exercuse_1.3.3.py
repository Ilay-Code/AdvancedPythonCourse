import functools


def is_funny(string):
    return string.replace('h', '').replace('a', '') == ''


def main():
    print(is_funny("hahahahahaha"))


if __name__ == '__main__':
    main()
