def log_decorator(func):
    """Decorator to log the execution of a function."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_decorator
def display_welcome_message():
    """Display a welcome message for the library system."""
    print("Welcome to the Library System!")