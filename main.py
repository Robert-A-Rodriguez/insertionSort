def insertionSort(array):
    for i in range(1, len(array)): #we start at index 1 because index 0 is technically already sorted
        j = i
        #loop backwards through array
        # the main point of this loop is to compare an element with the previous one to see if it is > or <
        # say array is [1,2,3,5,4] while there are numbers not sorted keep going in this while loop
        while j>0 and array[j] < array[j-1]: #while j hasn't reached the very beginning of the array and while there are still numbers left to be sorted
            swap(j, j-1, array) #swap current J with the index before it
            j-=1    #decrement J to keep track of the number we are trying to insert
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


myArr = [2,3,4,1,54]
print(insertionSort(myArr))


