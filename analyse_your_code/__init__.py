list_comp = list(range(0, 10000000))


def list_test():
    arr = []
    for x in list_comp:
        arr.append(x)
    return arr


def print_output():
    print('completed')


def main():
    list_test()
    print_output()