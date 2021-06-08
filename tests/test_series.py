from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series



def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_2():
    assert fibonacci(2) == 1

def test_fibonacci_3():
    assert fibonacci(3) == 2

def test_fibonacci_6():
    assert fibonacci(6) == 8

def test_lucas_0():
    assert lucas(0) == 2

def test_lucas_1():
    assert lucas(1) == 1

def test_lucas_2():
    assert lucas(2) == 3

def test_lucas_3():
    assert lucas(3) == 4

def test_lucas_6():
    assert lucas(6) == 18

# test fibonacci
def test_sum_series_3_0_1():
    assert sum_series(3,0,1) == 2

# test lucas
def test_sum_series_3_2_1():
    assert sum_series(3,2,1) == 4

# test any series
def test_sum_series_3_3_4():
    assert sum_series(3,3,4)==11

def test_sum_series_3_2_3():
    assert sum_series(3,2,3)==8

def test_sum_series_3_5_2():
    assert sum_series(3,5,1)==7

def test_sum_series_4_7_12():
    assert sum_series(4,7,12)==50

# test if there is no a & b 
def test_sum_series_3():
    assert sum_series(3)==2

def test_sum_series_6():
    assert sum_series(6)==8
