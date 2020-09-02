# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr

'''
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
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

# insertion sort
# you have part array thats sorted
# take next unsorted el
# insert it into sorted part array
# swap it in place / shift other els to the right
# compare to each of els in sorted part of array going biggest ==> smallest
# otherwise if sorted el is < current:
    # found right place insert it
# else get to end
    # insert at beginning
# 1 how we know where to insert it?
# 2 how move other elements over?

nums = [63,64,84,97,29,8,83,46,58,49,45,26,13]

def insertion_sort(arr):
    # part of arr is sorted
    # have an index to 1st el thats unsorted
    first_unsorted_index = 1
    # take next unsorted el
    # store el trying to insert into a var
    current_el = arr[first_unsorted_index]
    # compare it to each of the els in sorted part of array going from biggest --> smallest
    sorted_index = first_unsorted_index - 1
    while
    # iif sorted el bigger than current, shift sorted el right by 1
        if arr[sorted_index] > current_el:
            arr[sorted_index + 1] = arr[sorted_index]
            sorted_index = sorted_index - 1
        # other wise sorted el is < current:
        elif arr[sorted_index] < current_el:

        # found right place and can insert it ther else get to end
        elif 