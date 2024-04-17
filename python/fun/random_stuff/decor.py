import time


def timed(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")

    return wrapper


@timed
def do_something():
    # test comment
    time.sleep(1.5)


@timed
def do_something_else():
    time.sleep(2)


do_something()
do_something_else()
print("Done.")
