# https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html


# Pivot is the first element
def quickSort(arr):
    # calling the recursive function
   quickSortHelper(arr,0,len(arr)-1)


# Recursive function
def quickSortHelper(arr,first,last):
    # Base case
        # if the array length < 1, list is already sorted
   if first<last:

       # Defining a split point
       splitpoint = partition(arr,first,last)

       # Call the recursive function on the sub-arrays
       quickSortHelper(arr,first,splitpoint-1)
       quickSortHelper(arr,splitpoint+1,last)

# Function for partitioning the array around the pivot
def partition(arr,first,last):
   # Defining pivot (first array element)
   pivotvalue = arr[first]
   # Left partition marker is the first element remaining 
   leftmark = first+1
   # Right partition marker is the last element remaining 
   rightmark = last

   done = False
   while not done:
       # Move the left marker to the right until the element > pivot
       while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       # Move the right marker left until the element < pivot
       while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       # Stop if the second marker is less then the first one 
       if rightmark < leftmark:
           done = True
       else:
       # Swap the values that are out of place 
           temp = arr[leftmark]
           arr[leftmark] = arr[rightmark]
           arr[rightmark] = temp
   # Swap the values 
   temp = arr[first]
   arr[first] = arr[rightmark]
   arr[rightmark] = temp

   return rightmark