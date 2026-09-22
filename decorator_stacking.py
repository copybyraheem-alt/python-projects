def bold(func):
    def wrapper():
        return f"***{func()}***"
    return wrapper

def shout(func):
    def wrapper():
        result=func()
        return result.upper()
    return wrapper


@bold
@shout
def greet():
    return "hello world"


print(greet())
