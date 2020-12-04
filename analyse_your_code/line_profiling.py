from line_profiler import LineProfiler
from analyse_your_code import list_test

if __name__ == "__main__":
    lp = LineProfiler()
    lp_wrapper = lp(list_test)
    lp_wrapper()
    lp.print_stats()
