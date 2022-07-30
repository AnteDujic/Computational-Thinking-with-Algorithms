# To calculate the running time
import time
# To work with dataframe and plot
import numpy as np
# To generate random integers
import pandas as pd
# To plot
import matplotlib.pyplot as plt

# Sorting algorithm scripts
import bubbleSort
import selectionSort
import mergeSort
import quickSort
import countingSort

# Random number generator
rng = np.random.default_rng()

# Dictionary (for accessing algorithm scripts accordingly)
algorithms = {
            "Bubble Sort": bubbleSort.bubbleSort, 
            "Selection Sort": selectionSort.selectionSort,
            "Merge Sort": mergeSort.mergeSort,
            "Quick Sort": quickSort.quickSort,
            "Counting Sort": countingSort.countingSort
            }


# Input sizes
size = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
# Number of runs
runs = 10

# Arrays for appending
results = []            # Running time
sorting_algorithm = []  # Algorithm
nsize = []              # Input size

# Benchmarking function
def benchmark():
    # Iterate through the dict
    for a in algorithms:
        print (f"\nSorting with {a}...")    # Print current algorithm name

        # Iterate through size array
        for i in size: 

            # Loop 10 times (runs times)
            for r in range (runs):
                # Select the algorithm
                algorithm = algorithms[a]
                # Generate a random array of integers in range 0 - 100 of selected size
                arr = rng.integers(100, size = i)
                
                # Store the time (before the function runs)
                start_time = time.time()
                # Run the selected function
                algorithm(arr)
                # Store the time (when function finishes)
                end_time = time.time()
                # Calculate the function running time
                time_elapsed = (end_time - start_time)*1000
                
                # Apeending current values to arrays
                results.append(time_elapsed)    # Running time
                sorting_algorithm.append(a)     # Algorithm
                nsize.append(i)                 # Input size

    # Create a dataframe and store values
    df = pd.DataFrame ({
                    "Sorting Algorithm":sorting_algorithm,
                    "Time": results,
                    "Input size": nsize
                    })

    # Round the values to 2 decimal places
    df = df.round(2)    # 2 dec places will give 3 decimal places in the mean below
    # df.to_csv("AllRunningtime.csv")   # saving to .csv

    # Formatting df for neat output
    # pivot_table formats df to "excel" visual style
        # also calculates mean by default
    table = pd.pivot_table(df, index="Sorting Algorithm", columns="Input size") # value = "mean" default
    table = table.rename_axis("", axis=0)   # Removing "Sorting algorithm" column name from final table
    table.columns = table.columns.droplevel(level=0)    # Rows in table are multiindexed, remove one level
    table = table.reindex(["Bubble Sort", "Selection Sort", "Merge Sort", "Quick Sort", "Counting Sort"])   # df outputs alphabetically by default
    
    # table.to_csv("AvarageRunningtime.csv")    # save formatted table to .csv

    print ("\nSORTING ALGORITHMS RUNNING TIME:")
    print (table)

    # Plotting
    ax = table.T.plot(kind="line", marker = ".")
    plt.title("SORTING ALGORITHM AVERAGE RUNNING TIME")
    plt.ylabel ("Running time (milliseconds)")
    # plt.savefig("Running time_All.png")       # save plot image
    plt.show()
    

# Run the function
if __name__ == "__main__":
    benchmark()


