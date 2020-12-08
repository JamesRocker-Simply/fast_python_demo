Fast Python
---------------------

 * Introduction
 * Installation
 * Scripts
 * Timing
 * Benchmarking
 * Cython
 
 ## Introduction
 The fast_python repo is design to show case some code benchmarking tools, some performance improvement techniques ranging from easy to hard. This is to showcase the findings for Higher Performance Python Project talk.
 
 When you look through the code remember, code benchmark performance is not the only performance you need to worry about as a developer. Limitations added from some of these techniques and additional complexity can be detrimental to your projects success. 
 
## Installation
Clone the repo

In your virtual environment, install the requirements with
 
    pip install requirements.txt


## Scripts
Either open the project in an IDE or you can run the scripts through the commandline by just executing the following in your terminal

    python3 <script file>

e.g. 

    python3 analyse_your_code/timing

 
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