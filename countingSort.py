# https://stackabuse.com/counting-sort-in-python/

def countingSort(arr):
    # Finding the maximum element in the array
    maxElement= max(arr)

    # Set the lenght of the temp array to the array lenght + 1
    countArrayLength = maxElement+1

    # Initialize the counting array
    countArray = [0] * countArrayLength

    # Iterate throught the array
    for el in arr:
        # Set the count for every element by 1
        countArray[el] += 1

    # Loop the range of the count array
    for i in range(1, countArrayLength):
        # For each element in the countArray, 
        # sum up its value with the value of the previous 
        # element, and then store that value 
        # as the value of the current element
        countArray[i] += countArray[i-1] 

    # Calculate element position based on the count array values
    outputArray = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        currentEl = arr[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1
    #print (outputArray)    
    return outputArray
