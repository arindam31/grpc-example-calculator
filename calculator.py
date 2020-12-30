#

import math


def square(num):
    res = num * num
    return res


def square_root(num):
    res = math.sqrt(num)
    return res


def multiplier(numlist, name):
    mul = 1
    for num in numlist:
        mul = mul * num.value
    print(f'Result of list {name}')
    return mul


if __name__ == "__main__":
    print(multiplier([1, 2, 3, 4]))
