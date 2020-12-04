from really_fast_tuning.multiprocess_directory import defs

if __name__ == "__main__":
    output = map(defs.f, [1, 2, 3])
    print(list(output))