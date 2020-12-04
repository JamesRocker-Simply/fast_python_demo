import timeit
list_comp = list(range(0, 10000000))
set_list = set(list_comp)
tuple_list = tuple(list_comp)
number_to_find = 9000000

list_test = """
def list_test():
    for x in list_comp:
        print(x)
        """

set_test = """
def set_test():
    for x in set_list:
        print(x)
        """

tuple_test = """
def set_test():
    for x in tuple_list:
        print(x)
        """

list_in_test = """
def number_in_list():
    return number_to_find in tuple_list
"""

set_in_test = """
def number_in_set():
    return number_to_find in set_list
"""

tuple_in_test = """
def number_in_tuple():
    return number_to_find in tuple_list
"""


if __name__ == "__main__":
    print("Looping through")
    print(f'Mutable List testing - {timeit.timeit(list_test)}')
    print(f'Immutable Set testing - {timeit.timeit(set_test)}')
    print(f'Immutable Tuple testing - {timeit.timeit(tuple_test)}')
    print("Object In list")
    print(f'Mutable List testing - {timeit.timeit(list_in_test)}')
    print(f'Immutable Set testing - {timeit.timeit(set_in_test)}')
    print(f'Immutable Tuple testing - {timeit.timeit(tuple_in_test)}')
