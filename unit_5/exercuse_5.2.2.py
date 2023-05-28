numbers = iter(range(1, 101))

while True:
    try:
        num1 = next(numbers)
        num2 = next(numbers)
        num3 = next(numbers)
        print(num3)
    except StopIteration:
        break