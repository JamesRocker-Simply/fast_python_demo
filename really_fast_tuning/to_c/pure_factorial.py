def test(x):
    y = 1
    for i in range(1, x+1):
        y *= i
    return y

# running %timeit %run really_fast_tuning/to_c/c_based_factorial.py  shows this almost 2 and a half seconds slower


if __name__ == "__main__":
    test(100000)