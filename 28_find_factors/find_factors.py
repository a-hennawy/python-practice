def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    n = 1
    factor_lst = []
    while (n <= num):
        if num % n == 0:
            factor_lst.append(n)
        n += 1
    return factor_lst
