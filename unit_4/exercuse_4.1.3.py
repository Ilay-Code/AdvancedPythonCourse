def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_generator(n):
    number = n + 1
    while True:
        if is_prime(number):
            yield number
        number += 1


def first_prime_over(n):
    primes = prime_generator(n)
    return next(primes)


def main():
    print(first_prime_over(1000000))


if __name__ == '__main__':
    main()
