import datetime
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called at {datetime.datetime.now()}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def my_func():
    print("I am a decorated function")

my_func()