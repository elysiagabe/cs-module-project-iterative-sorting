def linear_search(arr, target):
    # Your code here
    # loop thru every item in array
    for i in range(0, len(arr)):
        # if the target is found
        if arr[i] == target:
            # return the index of the target value (per test requirement)
            return i
    # else return -1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # set up beginning & end of part of array that's being searched (initialize w/beginning & end of list)
    first = 0
    last = len(arr) - 1

    while first <= last:
        # find midpoint
        midpoint = (first + last) // 2
        # if target is equal to midpoint value, 
        if arr[midpoint] == target:
            # return index of found item
            return midpoint
        # if midpoint value is greater than target, throw out right side of list
        if arr[midpoint] > target:
            last = midpoint - 1
        # otherwise if midpoint value is less than target, throw out the left side
        else: 
            first = midpoint + 1

    return -1  # not found
