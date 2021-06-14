def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def double(n):
    """
    >>> double(5)
    10
    """
    return n * 2


def main():

    print(summation(3, double))


if __name__ == '__main__':
    main()
