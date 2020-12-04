import multiprocess as mp
from really_fast_tuning.multiprocess_directory import defs


if __name__ == '__main__':
    to_exec = defs.f
    cpu_pool = mp.Pool(4)
    with cpu_pool as p:
        print(p.map(to_exec, [1, 2, 3]))
