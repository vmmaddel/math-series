from math_series.fibonacci import fibonacci

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_2():
    assert fibonacci(2) == 1

def test_fibonacci_5():
    assert fibonacci(5) == 5