import timeit


def standard_loops():
    return_list = []
    for i in sentence:
        if i in 'aeiou':
            return_list.append(i)
    return return_list


sentence = 'the rocket came back from mars'
comprehension = [i for i in sentence if i in 'aeiou']

if __name__ == "__main__":
    print(min(timeit.Timer(str(comprehension)).repeat(100)))
    print(min(timeit.Timer(str(standard_loops())).repeat(100)))
