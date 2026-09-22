def highlight(func):
    def wrapper():
        print ("********************")
        func()
        print ("********************")
    return wrapper

@highlight
def show_name():
        print("Python")


show_name()