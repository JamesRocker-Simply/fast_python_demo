import numpy as np
import timeit

sample = np.random.choice(10, size=1000000)  # random sample of 1000000 numbers between 0 and 10


def unique_items(random_list):
    output = []
    for x in random_list:
        if x not in output:
            output.append(x)
    return output


if __name__ == "__main__":
    print(timeit.timeit(str(unique_items(sample))))
    print(timeit.timeit(str(list(set(sample)))))  # Yay it's faster
