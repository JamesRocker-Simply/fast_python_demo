from memory_profiler import profile

list_comp = list(range(0, 100000))


@profile()
def test_main():
    arr = []
    for x in list_comp:
        arr.append(x)
    return arr


if __name__ == "__main__":
    test_main()
