from functools import wraps



def log_activity(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        print(f"Function {func.__name__} is called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wapper
    
@log_activity
def brew_chai(type , milk="no"):
    print(f"Brewing {type} Chai with {milk} milk")
brew_chai("Masala")
