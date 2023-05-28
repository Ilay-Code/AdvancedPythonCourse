def raise_stop_iteration():
    y = [1, 2, 3]
    x = iter(y)
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())


def raise_zero_division():
    x = 10 / 0


def raise_assertion_error():
    assert 2 + 2 == 5


def raise_import_error():
    import ilay_mo


def raise_key_error():
    my_dict = {"key": "value"}
    value = my_dict["nonexistent_key"]


def raise_syntax_error():
    eval("print 'SyntaxError exception'")


# for this error you need to click shift+tab on print('1')
def raise_indentation_error():
    site = 'ilay'
    if site == 'ilay':
        print('1')
    else:
        print('2')

    print('3')


def raise_type_error():
    x = "hello" + 5


def main():
    try:
        raise_stop_iteration()
    except StopIteration as e:
        print("Caught StopIteration exception:", str(e))

    try:
        raise_zero_division()
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError exception:", str(e))

    try:
        raise_assertion_error()
    except AssertionError as e:
        print("Caught AssertionError exception:", str(e))

    try:
        raise_import_error()
    except ImportError as e:
        print("Caught ImportError exception:", str(e))

    try:
        raise_key_error()
    except KeyError as e:
        print("Caught KeyError exception:", str(e))

    try:
        raise_syntax_error()
    except SyntaxError as e:
        print("Caught SyntaxError exception:", str(e))

    try:
        raise_indentation_error()
    except IndentationError as e:
        print("Caught IndentationError exception:", str(e))

    try:
        raise_type_error()
    except TypeError as e:
        print("Caught TypeError exception:", str(e))


if __name__ == '__main__':
    main()
