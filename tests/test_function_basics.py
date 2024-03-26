"""Testing suite for function basics"""

from functions import function_basics

import random
import time

import pytest

def random_number():
    """Generate random number in [0.1, 10)"""
    return random.random() * 10 + 0.1

def test_print_result(capsys):
    #generate random result
    result = random_number()
    
    function_basics.print_result(result)
    captured = capsys.readouterr()
    
    #test whether there is a message along with the result
    assert captured.out.replace("\n", "") != str(result)
    #test whether the result is included in the printed message
    assert str(result) in captured.out


def test_add(capsys):
    #generate random numbers
    a = random_number()
    b = random_number()

    result = a + b

    function_basics.add(a, b)
    captured = capsys.readouterr()

    #Check whether the correct result is in the printed message
    assert str(result) in captured.out


def test_multiply(capsys):
    #generate random numbers
    a = random_number()
    b = random_number()

    result = a * b

    function_basics.multiply(a, b)
    captured = capsys.readouterr()

    #Check whether the correct result is in the printed message
    assert str(result) in captured.out

def test_subtract():
    #generate random numbers
    a = random_number()
    b = random_number()
    
    result = a - b

    assert function_basics.subtract(a, b) == result

def test_divide():
    #generate random numbers
    a = random_number()
    b = random_number()
    
    result = a / b

    assert function_basics.divide(a, b) == result

def time_millis():
    return round(time.time() * 1000)

@pytest.mark.timeout(1)
def test_timer_waits_correct_time():
    """Test to make sure that the timer waits the specified amount of seconds"""
    
    seconds = 0.3
    
    start = time_millis()
    function_basics.timer(seconds, "")
    
    #calculate the difference in seconds
    diff = (time_millis() - start) / 1000

    #allow for an error of 5%
    if abs(seconds - diff) / seconds > 0.05:
        pytest.fail(f"Timer waited for {diff} seconds (target: {seconds} seconds)")


@pytest.mark.timeout(1)
def test_timer_prints_message(capsys):
    """Test that checks whether the specified message is printed"""
    message = "Timer has expired"
    seconds = 0.1
    
    function_basics.timer(seconds, message)
    captured = capsys.readouterr()

    assert message in captured.out
