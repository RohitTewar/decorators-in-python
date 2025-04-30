#cache return value 
import time

def cache (func):
    cache_value = {}
    print(cache_value)
    # This is a decorator that caches the return value of a function.
    def wrapper(*args):
        if args in cache_value:
            
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(4,5)) # This will take 4 seconds to run
print(long_running_function(4,5)) # This will return the cached value immediately
print(long_running_function(3,8)) # This will return the cached value immediately