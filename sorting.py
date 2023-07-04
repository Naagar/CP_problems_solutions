# sorting.py
# bubble sort
# selection sort
# insertion sort
# bucket sort
# merg sort
# quick sort
# heap sort

# def: arrange the data in ascending and decending order

# In-place : no extra space needed e.g., bubble sort
# Out-place: extra space
# Stable sorting: sequence of same values does not change, e.g., insertion sort
# Unstable sorting: sequence of same values does change, e.g., Quick sort
# # increasing order, non-increasing order, decreasing order, non-decreasing order 

# bubble, swap adjcent elements

# selection, find the min/max and move it to sorted paert of array (unsorted to sorted)

# insertion, devide the array into teo parts, take frist el from unsorted array and place it on the correct position
        #  in the sorted array, repeat
# bucket, crate buckets and distribute elements pf arr into buckets, sort buckets independently, and merg buckets
    # no of buckets = round(sqrt(len(arr)))
    # appropriate buckets = ceil(value * numbers of buckets / max value)
    # use when data is distributed over a range uniformly

# merge: Devide and conquer algo.
    # devide the arr into two half 
    
# quick,
# heap

# which one to select:
    # stablility,
    # spcae efficent,
    # time efficent

# Bubble sort: compare adjcent pair
from typing import Mapping


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) -i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i +1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
def insertion_sort(arr):
    arr_sort = []
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = temp
    print(arr)
import math
def bucket_sort(arr):
    num_buckets = round(math.sqrt(len(arr)))
    max_value= max(arr)
    arr_temp =  []
    for i in range(num_buckets):
        arr.append([])

    for j in arr:
        index_bucket = math.ceil(j*num_buckets/max_value)
        arr_temp[index_bucket-1].append(j)

    for i in range(num_buckets):
        arr_temp[i] = insertion_sort(arr_temp[i])

    k = 0
    for i in range(num_buckets):
        for j in range(len(arr_temp[i])):
            arr[k] = arr_temp[i][j]
            k += 1
    return arr


c_list = [2,1,4,9,2,3,5,5,9,1]
bucket_sort(c_list)
