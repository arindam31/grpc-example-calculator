import math


def square(num: int) -> int:
    """Function for calculating square

    :param num
    :return int
    """
    res = num * num
    return res


def square_root(num: int) -> float:
    """Function for calculating squareroot

    :param num int
    :return int
    """
    res = math.sqrt(num)
    return res


def multiplier(numlist: list, name: str):
    """Function for multiplying all numbers in a list

    :param numlist list
    :return int/float
    """
    mul = 1
    for num in numlist:
        mul = mul * num.value
    print(f'Result of list {name}')
    return mul


if __name__ == "__main__":
    print(multiplier([1, 2, 3, 4]))
