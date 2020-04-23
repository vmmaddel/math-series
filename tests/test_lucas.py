from math_series.lucas import lucas

def test_lucas_0():
    assert lucas(0) == 2

def test_lucas_1():
    assert lucas(1) == 1

def test_lucsa_2():
    assert lucas(2) == 3

def test_lucsa_5():
    assert lucas(5) == 11
