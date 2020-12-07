from line_profiler import LineProfiler

profile = LineProfiler()
list_comp = list(range(0, 1000000))


@profile
def list_test():
    arr = []
    for x in list_comp:
        arr.append(x)
    return arr


if __name__ == "__main__":
    list_test()
    profile.print_stats()
