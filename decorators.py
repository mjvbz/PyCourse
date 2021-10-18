def word(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the functions.")
    return wrapper

@word
def hello():
    print("Hello, world!")

hello()

 

