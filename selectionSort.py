# https://stackabuse.com/selection-sort-in-python/


def selectionSort(arr):

    # Defining the size of the array
    n = len(arr)

    # Loop to access each array element
    for i in range(n-1):

        # Set the first element to be the minimum
            #other elements will be compared to it
        min_index = i

        # Loop throught the remaining array elements
        for j in range(i+1, n):

            # If the element at j is lower then the minimum
            if arr[j] < arr[min_index]:
                # Assign it as a new minimum
                min_index = j

        # After finding the lowest element, spap with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]