"""
A decorator in python is a function that receives another function as input, adds some additional functionality(decoration) into it and returns the same function.

This above behaviour is possible only because functions in python are first class citizens.

"""

# Write a function which will act as decorator, and will calculate the execution time of any function
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print('time taken by ', func.__name__, ' is ', time.time()-start, ' secs')
    return wrapper
    
@timer
def hello():
    print('Hello World')

@timer    
def square(num):
    print(num**2)

hello()
square()
     
"""
What happend above is, at execution time  line 18 to 20 will be replaced by hello = timer(hello) and later when i am calling hello() i am actually calling the function reference, pointing by the hello i.e. wrapper
"""    

