# COMPUTATIONAL THINKING WITH ALGORITHMS | 2022
### AUTHOR: ANTE DUJIC
<hr style="border:2px solid gray"> </hr>

This repository contains a project done for Computational Thinking with Algorithms module on ATU, Ireland. The aim of the project is to write an application which will be used to benchmark five different sorting algorithms.

### HOW TO RUN THIS PROJECT?
***

1. Clone this repository
2. Download [Anaconda](https://docs.anaconda.com/anaconda/install/windows/)
3. Download [cmder](https://cmder.net/)
4. Run the *benchmark.py*
    - NOTE: The time required for this application to run depends on the machine it is run on.

### BENCHMARK REPORT
***

There are two ways to analyse algorithm efficiency, a priory and a posteriori analysis. Benchmarking is a posteriori analysis, meaning it is an empirical method used to compare the relative performances of the algorithms. The performance of an algorithm depends on the various hardware and software characteristics. For this reason, there are multiple statistical runs done on the same machine. This provides the best possible representation of the algorithm performance for an average user.
Benchmarking for this project is done using an application created in Python – *benchmark.py*. 

The sorting algorithms benchmarked are:
- Two simple comparison-based sorts
    - Bubble Sort
    - Selection Sort
- Two efficient comparison-based sorts
    - Merge Sort
    - Quick Sort
- A non-comparison sorts
    - Counting Sort

Each algorithm code is written in a separate script (*bubbleSort.py, selectionSort.py, mergeSort.py, quicksort.py, and countingSort.py*).

The table below shows the benchmark results. The output are average times in milliseconds calculated running each algorithm 10 times for different input sizes, in the range from 100 elements to 10 000 elements.

![](https://github.com/AnteDujic/Computational-Thinking-with-Algorithms/blob/main/Images/table.png)

The graphs below show the average running times for tested algorithms. Because running times of the Simple sorting algorithms are much higher than the other tested algorithms, and it is impossible to tell the difference between the remaining algorithms, there are 2 separate graphs, the first showing all five sorting algorithms, and the second one with Merge, Quick and Counting Sort algorithms only.

![](https://github.com/AnteDujic/Computational-Thinking-with-Algorithms/blob/main/Images/Running%20time_All.png)

![](https://github.com/AnteDujic/Computational-Thinking-with-Algorithms/blob/main/Images/Running%20time_MQC.png)


It is clearly visible from the first graph that Bubble sort is by far the slowest of the Five sorting algorithms. It is followed by a slightly faster, but still very slow Selection sort. Both Bubble and Selection sort have an average running time of n2. Merge sort and Quick sort algorithms have average time complexity of n log n. Same as for the simple sorting algorithm, this is clearly visible from the graph above. We can also see how Quick sort performs better than the Merge sort on the smaller input sizes, while Merge sort is more efficient on the input sizes with larger values. It is also visible how the efficient sorting algorithms have better running times than the simple sort ones, but are still much slower than the Counting sort. Counting sort has the average time n+k. It is the fastest of all Five sorting algorithms introduced in this project.

Full benchmark report can be seen on the following link: https://github.com/AnteDujic/Computational-Thinking-with-Algorithms/blob/main/Benchmark%20Report.pdf.