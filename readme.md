Fast Python
---------------------

 * Introduction
 * Installation
 * Scripts
 * Timing
 * Benchmarking
 * Cython
 
## Installation
Clone the repository using 

In your environment, install the requirements with
 
    pip install requirements.txt

Then either open the project in an IDE or you can run the scripts through the commandline

## Scripts
Most of the scripts in this project can be run simply by executing in an IDE or by using 

    python3 <script_file.py>
 
 
## Timing 
To run the timing cli, the easiest way is through Ipython in your terminal

    %timeit %run really_fast_tuning/to_c/c_based_factorial.py
    %timeit %run really_fast_tuning/to_c/pure_factorial.py

running these two commands can be used to demo the timing difference between the C based factorial code and then the pure python based version
 
 ## Benchmarking
If you are interested in the benchmarking side of the repository then the following commands will be useful. Perform these in your terminal 

To just perform the unit tests with benchmarks

    pytest 

To test the performance and save the results. This will save them to a directory at the top of the project called `.benchmarks` with the results in json format

    pytest --benchmark-autosave
    
You can also compare specific results with the benchmark results passed after compare
 
    pytest-benchmark compare 0001 0002 0003 0004
 
or compare all of them using 
 
    pytest-benchmark compare
 
Finally, you can build a histogram comparing the outputs by chaining `--histogram` to the end which will create an svg in the project root
 
    pytest-benchmark compare --histogram
 
Have a play around with some of the unit tests. See if you can get it to fail due to a benchmark issue using
 
    --benchmark-compare-fail=min:5%
 
## Cython
In the `really_fast_tuning/to_c` directory we have a setup file and .pyx file which is a source code file written in Pyrex, which is a Python-like language for writing Python modules with a C-like synatx.
By running the below command, we build 

    python setup.py build_ext --inplace

There are other ways to build cython code but this is the easiest in my opinion. 