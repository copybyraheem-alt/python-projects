from functools import wraps


def highlight(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("********************")
        result = func(*args, **kwargs)
        print("********************")
        return result
    return wrapper


@highlight
def show_name():
    print("Python")


if __name__ == "__main__":
    show_name()
