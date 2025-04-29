#timing function execution time
import time
def timer(func):
    def wrapper (*args, **kwargs):
        start= time.time()
        result = func(*args, **kwargs)
        end= time.time()
        print(f"functon{func.__name__} ran in {end-start} this time")
        return result
    return wrapper

@timer #decorator
def example_function(n):
    time.sleep(n)

example_function(2)
#example_function(2) #decorator is applied to this function
#time taken to execute this function is 2 seconds