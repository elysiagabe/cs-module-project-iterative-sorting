# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # this is the current element we're looking at (first unsorted element)
        cur_index = i 
        # set the smallest_index to cur_index b/c nothing to compare to yet
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # loop thru the rest of the unsorted items (all items to the right of the current element we're looking at)
        for j in range(cur_index + 1, len(arr)):
            # if one of these elements is less than the current minimum, update smallest_index
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    finished = False
    # keep looping thru pairs of items in array until there are 0 swaps made
    while not finished: 
        # initialize swap counter
        swap_counter = 0
        # loop thru neighboring pairs (i = item to left, j = item to right)
        for i in range(0, len(arr) - 1):
            j = i + 1
            # if item to left is greater than item to right
            if arr[i] > arr[j]:
                # swap their positions
                arr[i], arr[j] = arr[j], arr[i]
                # incrememnt swaps counter
                swap_counter += 1
        # if no swaps are made
        if swap_counter == 0: 
            # then exit the while loop, finished sorting
            finished = True

    return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
