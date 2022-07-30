# REF: https://www.geeksforgeeks.org/python-program-for-bubble-sort/


def bubbleSort(arr):

    # Defining the size of the array
    n = len(arr)

    # Loop to access each array element
    for i in range(n-1): 

        # Loop to compare array elements
        for j in range(0, n-i-1):

            # Compare the two adjacent elements
            if arr[j] > arr[j + 1] :

                # Swap the elements if the above comparison is true
                arr[j], arr[j + 1] = arr[j + 1], arr[j]