import time

def factorial(n):
    """Calculates the factorial of a number using loops.

    Args:
        n (int): Positive number to take the factorial of

    Returns:
        The factorial of n
    """
    result = 1
    # Loop over all values of i in [1, n]
    for i in range(1, n + 1):
        result *= i
    return result
    
    return result

def timeit(func, arg):
    """Function that takes a function (func), executes it, and measures the time it took the function to run.

    Args:
        func (function): Function to be timed
        arg: A generic parameter to be passed to func

    Returns:
        Execution time of func in milliseconds
    """
    start = time.time()
    func(arg)
    end = time.time()
    execution_time = (end - start) * 1000 
    return execution_time

def calculate_e(max_iterations):
    """Function that calculates Euler's number by evaluating the power series.

    Args:
        max_iterations (int): Point at which the power series should be cut off (upper limit of the summation)

    Returns:
        The approximate value of Euler's number (e)
    """
    e = 0
    for n in range(max_iterations):
        e += 1 / factorial(n) 

    return e

def calculate_pi(max_iterations):
    """Function that calculates Pi by evaluating the Leibniz formula.

    Args:
        max_iterations (int): Point at which the power series should be cut off (upper limit of the summation)

    Returns:
        The approximate value of Pi (π)
    """
    pi = 0
    for n in range(max_iterations):
        # the Leibniz formula
        term = (-1) ** n / (2 * n + 1)
        pi += term

    #get an approximation of Pi
    pi *= 4

    return pi


def f(x):
    """Function that returns the value of the mathematical function f(x) = x^2 + 2x + 3

    Args:
        x (float): Point at which the function should be evaluated

    Returns:
        The value of the function f(x) at the specified point x
    """
    return x**2 + 2 * x + 3

def main_menu(max_iterations):
    """Function that prints a nice overview of the program's features and tells the user how to access them.
    Queries for an input, runs the respective function if the input is valid and returns True (otherwise returns False).

    The menu should enable the user to choose from the following options:
        - Calculate and print Euler's number
        - Calculate and print Pi
        - Calculate and print the value of the function f(x) = x**2 + 2 x + 3 at x = 2
        - Measure and print the time in milliseconds it took the algorithm to calculate e and Pi respectively

    Args:
        max_iterations (int): Maximum iterations that will be passed to the calculate functions

    Returns:
        True, if the input was valid, False otherwise
    """
    selection = input("Choose an option (1 - 4): ")

    if selection == "1":
        e = calculate_e(max_iterations)
        print(f"Euler's number is approximately: {e}")
        return True
    elif selection == "2":
        pi = calculate_pi(max_iterations)
        print(f"PI is approximately: {pi}")
        return True
    elif selection == "3":
        res = f(2)
        print(f"f(x): {res}")
        return True
    else:
        print("Invalid choice. Please try again.")
        return False

def print_main_menu():
    pass

def main(max_iterations=100):
    while True:
        print_main_menu()
        result = main_menu(max_iterations)
        if result == True:
            break
    print("Program exiting")


def factorial_recursive(n):
    """Calculate the factorial of a number using recursion.

    Args:
        n (int): Positive number to take the factorial of

    Returns:
        The factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)



#Check whether the program was run from the command line
if __name__ == "__main__":
    #if so, run the main function
    main(100)
