def main():
    # task 1
    with open("names") as file:
        longest_name = max(file.read().splitlines(), key=len)
    print(longest_name)
    # task 2
    with open("names") as file:
        name_lengths = sum(len(name) for name in file.read().splitlines())
    print(name_lengths)
    # task 3
    with open("names") as file:
        names = file.read().splitlines()
        shortest_length = min(len(name) for name in names)
        shortest_names = [name for name in names if len(name) == shortest_length]
    print('\n'.join(shortest_names))
    # task 4
    with open("names") as input_file, open("name_length.txt", "w") as output_file:
        output_file.write('\n'.join(str(len(name)) for name in input_file.read().splitlines()))
    # task 5
    length = int(input("Enter name length: "))
    with open("names") as file:
        names_of_length = [name for name in file.read().splitlines() if len(name) == length]
    print('\n'.join(names_of_length))


if __name__ == '__main__':
    main()
