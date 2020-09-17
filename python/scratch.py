def run_twice(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        fn(*args, **kwargs)

    return inner


@run_twice
def repeater(phrase):
    print(phrase)


repeater("Python")
