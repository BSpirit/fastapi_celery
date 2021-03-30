import time


def add(a: int, b: int) -> int:
    return a + b

def long_add(a: int, b: int, n: int = 20) -> int:
    time.sleep(n)
    return a + b
