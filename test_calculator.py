from my_lib import calculator


def test1():
    assert calculator(2, 3, '*') == 6


def test2():
    assert calculator(16.4, 4, '/') == 4.1


def test3():
    assert calculator(20, 7, 's') == 27


def test4():
    assert calculator(10, 0, '/') == float('inf')