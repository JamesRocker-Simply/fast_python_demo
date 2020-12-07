import timeit


list_comp = list(range(0, 1000000))
stringify = """
def list_test():
    arr = []
    for x in list_comp:
        arr.append(x)
    return arr
"""

if __name__ == "__main__":
    print(timeit.timeit(stringify))
