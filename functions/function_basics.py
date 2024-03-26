import time

def print_result(result):
    """Function that prints the result of a calculation with a message

    Args:
        result (float): The number that should be included in the printed message

    Example:
        >>> print_result(2.0)
        <<< The result is: 2.0
    """
    print(f"The result is: {result}")


def add(a, b):
    """Function that adds two numbers and prints the result
    
    Args:
        a (float): First number
        b (float): Second number

    """
    c = a + b
    print_result(c)


def multiply(a, b):
    """Function that multiplies two numbers and prints the result
    
    Args:
        a (float): First number
        b (float): Second number

    """
    c = a * b
    print_result(c) 

def subtract(a, b):
    """Function that subtracts two numbers and returns the result.

    WARNING: Note that printing and returning are two completely different
    things. In contrast to the previous two functions, here, the result
    must be returned, not printed. Please refer to the lecture notes if
    you are not sure of what to do.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        The result of the subtraction a - b

    """
    return a - b

def divide(a, b):
    """Function that divides two numbers and returns the result

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        The result of the division a / b

    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def timer(seconds, message):
    """Timer that waits for a given number of seconds before printing a message
    
    Args:
        seconds (float): Number of seconds to pass before message is printed
        message (str): Message to print after the timer has expired

    """
    time.sleep(seconds)
    print(message)
