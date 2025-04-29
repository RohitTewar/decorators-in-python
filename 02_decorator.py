#Debugging function calls
import time
# Decorators are a powerful and useful tool in Python that allows you to modify the behavior of a function or class.
# They are often used to add functionality to existing code in a clean and readable way.


def debug(func):
    def wrapper(*args, **kwargs):
        args_value= ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with arguments: {args_value} and keyword arguments: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

@debug
def hello_world():
    print("hello Anime fans!")

hello_world()
greet("Rohit",greeting="welcome")