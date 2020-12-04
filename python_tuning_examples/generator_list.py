import timeit

test_num = 1000000


def first_n_ret(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


output_tot = sum(first_n_ret(test_num))


def first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


output_gen = sum(first_n_gen(test_num))

if __name__ == "__main__":
    print(min(timeit.Timer(str(output_tot)).repeat(100)))  # outputs 100 timings to a list of the function being performed 1000000 times then selects the smallest time
    print(min(timeit.Timer(str(output_gen)).repeat(100)))
