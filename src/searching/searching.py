def linear_search(arr, target):
    # loop through the array
    for i in arr:
        # compare values
        if i == target:
             return True
        # else: keep looping
    # finish looping:
    # we didnt find it. return False

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    # look at middle
    # compare to middle
        # how get midpoint?
            # for whole array, len(arr) / 2 - 1
            # for subset of array: (start + end) // 2
    while end >= start:
        middle_index = (start + end) // 2
        middle_value = arr[middle_index]

        if target == middle_value:
            return True
        if target == middle_value:
            start = middle_index + 1
        if target < middle_value:
            end = middle_index - 1


    # if target == middle value:
        # return true
    # if target > middle value:
        # search right side
    # if target < middle value:
        # search left side
    # repeat
    # if not found return false
        # how know not found?
        # subset looking at has 0 or neg len
    # how rep subset / window were searching in?
        # start in & end index
        # start index + len of subarray
        # pass around slices of array - creates new array, use extra memory & time


    return -1  # not found
