def read_file(file_name):
    msg = ""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            msg = f"__CONTENT_START__\n{content}"
    except FileNotFoundError:
        msg = "__CONTENT_START__\n__NO_SUCH_FILE__\n"
    finally:
        msg += "__CONTENT_END__"
        return msg


def main():
    result1 = read_file("ex3.2.5")
    print(result1)
    result2 = read_file("ilay")
    print(result2)


if __name__ == "__main__":
    main()
