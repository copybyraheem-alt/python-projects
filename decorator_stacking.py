from functools import wraps


def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"***{func(*args, **kwargs)}***"
    return wrapper


def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@bold
@shout
def greet():
    return "hello world"


if __name__ == "__main__":
    print(greet())
