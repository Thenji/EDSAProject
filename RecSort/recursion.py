def sum_array(array):
    """
    Return sum of all items in array.

    Args:
        array: list or array-type object containing numerical values.

    Returns:
        int: sum of the given array
    """
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    """
    Returns the nth term from a sequence where each number is the sum of the two preceding ones, starting from 0 and 1

    Args:
        int: nth position of sequence

    Returns:
        int: value of the nth term
    """
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

def factorial(n):
    """
    Returns the product of all positive integers less than or equal to n.

    Args:
        int: positive integer

    Returns:
        int: the product of all positive integers less than or equal to n

    """    
    if n == 0:
       return 1
    elif n == 1:
       return 1
    else:
       return n*factorial(n-1)


def reverse(word):
    """
    Returns word in reverse

    Args:
        string: a word

    Returns:
        string: the string in reverse
    """
    if len(word)==1:
        return word
    else:
        return word[-1] + reverse(word[:-1])
