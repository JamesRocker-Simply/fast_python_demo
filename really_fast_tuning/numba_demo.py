from numba import jit

random_list = tuple(range(0, 1000))  # Numba only likes tuples smaller than 1000 for looping


@jit(nopython=True)  # if True, uses numba and upon failure falls back to python interpreter. Use it where possible
def numba_mean(x):
    total = 0
    for xi in x:
        total += xi
    return total / len(x)


numba_output = numba_mean(random_list)
