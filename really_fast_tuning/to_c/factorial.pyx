cpdef int test(int x):
    # notice the slightly different syntax of declaring your variables
    cdef int y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y