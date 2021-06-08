def fibonacci(n):
    """
    Recursive function that solve Fibonacci series
    Arguments:
        n:integer -- the number of sequence we are looking for
    Returns:
        Number from the sequence that user inter it in Fibonacci
    """
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    """
    Recursive function that solve Lucas series
    Arguments:
        n:integer -- the number of sequence we are looking for
    Returns:
        Number from the sequence that user inter it in Lucas
    """
    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1)+lucas(n-2)

def sum_series(n,a=0,b=1):
    """
    Recursive function that solve a sum series similar to Fibonacci and Lucas
    Arguments:
        n:integer -- the number of sequence we are looking for
        a:optional integer or value of series at index 0
        b:optional integer or value of series at index 1
    Returns:
        Number with the user ine similar to Fibonacci and Lucas series 
        but could be any other math series based on the first two values
    """
    if n==0:
        return a
    if n==1:
        return b
    return sum_series(n-1,a,b)+sum_series(n-2,a,b)
    
