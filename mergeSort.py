# https://runestone.academy/ns/books/published/pythonds/SortSearch/TheMergeSort.html
# FIX [1] https://stackoverflow.com/questions/34889618/numpy-array-mergesort

def mergeSort(arr):
    if len(arr)>1:

        # Find the middle of the array
        mid = len(arr)//2
        
        # Create the two halves
            # Left from the mid point
        lefthalf = arr[:mid].copy() #[1]
            # Right from the mid point
        righthalf = arr[mid:].copy() #[1]

        # Calling the function on each half (recursion)
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # SORTING AND MERGING TWO HALVES

        i=0  # Initial index of the left array  
        j=0  # Initial index of the right array  
        k=0  # Initial index of the merged array 

        # Loop until the left and right array are empty 
        while i < len(lefthalf) and j < len(righthalf):

            # Compare the elements of the array
                # If the left element is smaller
            if lefthalf[i] <= righthalf[j]:
                # place this element in the merged array on index k
                arr[k]=lefthalf[i]
                i=i+1   # move to next index (left array)

                # if the right element is smaller
            else:
                # place this element in the merged array on index k
                arr[k]=righthalf[j]
                j=j+1   # move to next index (right array)
            k=k+1 # move to next index (merged array)

        # No elements left in right array
        # Loop until the left array is empty
        while i < len(lefthalf):
            # Place remaining elements of left array in merged array
            arr[k]=lefthalf[i]
            i=i+1   # move to next index (left array)
            k=k+1   # move to next index (merged array)

        # No elements left in left array
        # Place remaining elements of right array in merged array
        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1   # move to next index (right array)
            k=k+1   # move to next index (merged array)
            
    return (arr)
