def my_decorator(func):  # Takes a function as input
    def wrapper():       # The "wrapper" adds extra behavior
        print("~~ Before the function runs ~~")
        func()           # Calls the original function
        print("~~ After the function runs ~~")
    return wrapper       # Returns the wrapped function

# Apply the decorator to `say_hello`
@my_decorator
def say_hello():
    print("Hello!")

say_hello()