from loops import loops_basics

import random
import time
import math

import pytest
from unittest import mock

correct_e = 2.718281828459045
correct_pi = 3.141592653589793

def test_factorial():
    n = random.randrange(5, 50)
    
    correct_fact = math.factorial(n)
    fact = loops_basics.factorial(n)

    assert correct_fact == fact    

def test_timeit():
    seconds = random.random() / 2
    result = loops_basics.timeit(time.sleep, seconds)
    
    millis = seconds * 1000

    #allow for an error of 5%
    assert abs(result - millis)/millis <= 0.05

def test_calculate_e():
    e = loops_basics.calculate_e(100)

    #allow for a maximum tolerance of 5%
    assert abs(correct_e - e)/correct_e <= 0.05

def test_calculate_pi():
    pi = loops_basics.calculate_pi(100)

    #allow for a maximum tolerance of 5%
    assert abs(correct_pi - pi)/correct_pi <= 0.05

def test_f():
    x = random.random() * 100 - 50
    correct_f = x**2 + 2 * x + 3
    
    f = loops_basics.f(x)

    assert f == correct_f

@mock.patch("builtins.input", lambda option: "1")
def test_main_menu_option_1(capsys):
    e = loops_basics.calculate_e(100)
    result = loops_basics.main_menu(100)
    
    captured = capsys.readouterr()

    assert result
    assert len(str(e)) > 0
    assert str(e) in captured.out


@mock.patch("builtins.input", lambda option: "2")
def test_main_menu_option_2(capsys):
    pi = loops_basics.calculate_pi(100)
    result = loops_basics.main_menu(100)
    
    captured = capsys.readouterr()
    
    assert result
    assert len(str(pi)) > 0
    assert str(pi) in captured.out


@mock.patch("builtins.input", lambda option: "3")
def test_main_menu_option_3(capsys):
    f = loops_basics.f(2)
    result = loops_basics.main_menu(100)
    
    captured = capsys.readouterr()
    
    assert result
    assert len(str(f)) > 0
    assert str(f) in captured.out

@mock.patch("builtins.input", side_effect=["0", "5", "test"])
def test_main_menu_invalid_option(capsys):
    for i in range(3):
        assert not loops_basics.main_menu(100)

def test_factorial_recursive():
    n = random.randrange(5, 50)
    
    correct_fact = math.factorial(n)
    fact = loops_basics.factorial_recursive(n)

    assert correct_fact == fact    
