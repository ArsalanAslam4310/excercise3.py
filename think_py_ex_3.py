def do_twice(func, val):
    func(val)
    func(val)


def print_spam(value):
    print(value)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)


do_four(print_spam, "asad")
