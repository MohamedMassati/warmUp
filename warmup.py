"""Simple Python warm-up exercises."""


def sleep_in(weekday: bool, vacation: bool) -> bool:
    return not weekday or vacation


def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    return a_smile == b_smile


def sum_double(a: int, b: int) -> int:
    return (a + b) * 2 if a == b else a + b


def diff21(n: int) -> int:
    return (n - 21) * 2 if n > 21 else 21 - n


def parrot_trouble(talking: bool, hour: int) -> bool:
    return talking and (hour < 7 or hour > 20)


def makes10(a: int, b: int) -> bool:
    return a == 10 or b == 10 or a + b == 10


def near_hundred(n: int) -> bool:
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def pos_neg(a: int, b: int, negative: bool) -> bool:
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)
