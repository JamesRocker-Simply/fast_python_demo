import timeit
list_comp = list(range(0, 10000000))

# We are using these strings as functions to not consume the systems memory

enumerate_test = """
def enumerate_example():
    for n, z in enumerate(list_comp):
        print(n)
"""

range_test = """
def range_example():
    for n in range(len(list_comp)):
        print(n)
"""

in_loop = """
def raw_example():
    for n in list_comp:
        print(n)
"""

if __name__ == "__main__":
    print(timeit.timeit(enumerate_test))
    print(timeit.timeit(range_test))
    print(timeit.timeit(in_loop))
