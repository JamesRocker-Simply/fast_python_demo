import random
import timeit


def all_user(iterable):
    """
    Performs essentially the same function as the builtin all() command.
    If all items in the list are true, this will return true
    :param iterable:
    :return: true/false
    """
    for element in iterable:
        if not element:
            return False
    return True


def any_user(iterable):
    """
    Performs essentially the same function as the builtin any() command
    If an items in the list is true, this will return true
    :param iterable:
    :return: true/false
    """
    for element in iterable:
        if element:
            return True
    return False


# Built a list 100000 items of either true and false
bool_list = list(random.choice(("true", "false")) for _ in range(100000))

if __name__ == "__main__":
    print("---- Any test ----")
    print(f'Built in - {min(timeit.Timer(str(any(bool_list))).repeat(15))}')
    print(f'User func - {min(timeit.Timer(str(any_user(bool_list))).repeat(15))}')
    print("---- All test ----")
    print(f'Built in - {min(timeit.Timer(str(all(bool_list))).repeat(15))}')
    print(f'User func - {min(timeit.Timer(str(all_user(bool_list))).repeat(15))}')  # Oh...
