import timeit


def sum_two_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(min(timeit.Timer(str(sum_two_numbers(5, 5))).repeat(100)))
    assigned = sum_two_numbers(5, 5)
    print(min(timeit.Timer(str(assigned)).repeat(100)))
