def double_letter(my_str):
    def double_char(char):
        return char * 2

    return ''.join(map(double_char, my_str))


def main():
    print(double_letter("ilay"))


if __name__ == '__main__':
    main()
