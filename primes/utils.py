from mypy_extensions import i32


def get_primes(limit: i32, start: i32 = 2) -> list[i32]:
    """
    Returns a list of all prime numbers between the given start value and the limit value.

    Args:
    - limit (i32): The upper limit for the range of numbers to check for prime values.
    - start (i32): The starting value for the range of numbers to check for prime values. Default
      value is 2, as this is the smallest prime number.

    Returns:
    - A list of all prime numbers between the given start value and the limit value.

    Example:
    >>> get_primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]

    In the example above, the function returns a list of all prime numbers between 2 (the default
    start value) and 20 (the limit value). The output should be [2, 3, 5, 7, 11, 13, 17, 19], as these
    are the prime numbers in that range.
    """
    primes: list[i32] = []
    for x in range(start, limit):
        is_prime = True
        for y in range(2, x):
            if x % y == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes


def split_number(number: int, n: int) -> list[tuple[int, int]]:
    """
    Splits a given number into n parts of roughly equal size, returning a list of tuples
    representing the start and end indices of each part.

    Args:
    - number (int): The number to split.
    - n (int): The number of parts to split the number into.

    Returns:
    - A list of tuples, where each tuple contains two integers representing the start and
      end indices of a part. The start index is inclusive and the end index is exclusive.

    Example:
    >>> split_number(10, 3)
    [(2, 5), (5, 8), (8, 11)]

    In the example above, the number 10 is split into three parts of roughly equal size. The
    first part starts at index 2 and ends at index 5, the second part starts at index 5 and
    ends at index 8, and the third part starts at index 8 and ends at index 11.
    """
    quotient, remainder = divmod(number, n)
    if quotient == 0:
        return [(2, number)]
    parts = []
    start = 2
    for i in range(n):
        end = start + quotient
        if i < remainder:
            end += 1
        parts.append((start, end))
        start = end
    return parts
