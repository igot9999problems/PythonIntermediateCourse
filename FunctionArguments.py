def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)
print()


def list_to_args(a, b, c):
    print(a, b, c)

my_list = [2, 1, 3]
list_to_args(*my_list)
print()


def dict_to_args(c, f, d):
    print(c, f, d)

my_dict = {'c': 2, 'f': 5, 'd': 7}
print(dict_to_args(**my_dict))
print()


