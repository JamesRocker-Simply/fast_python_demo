random_list = tuple(range(0, 1000))


def just_mean(x):
    total = 0
    for xi in x:
        total += xi
    return total / len(x)


mean_output = just_mean(random_list)
