# Interview Question
# Find a number 
import numpy as np
my_arr =np.array([1,2,3,4,5,6,7,8,9])
def find_num(arr, n):
    for i in arr:
        if i == n:
            return True
        else:
            return False
print(find_num(my_arr, 4))

# # Finfing missing number
# my_list = [1,2,3,4,5,6,7,8,9]
# def find_miss_no(list, n:
#     sum_full = n * (n + 1)/2
#     sum_list = sum(list)
#     return (sum_full-sum_list)
# print(find_miss_no(my_list,10))

# Decimal to binary 

# def dec_to_bin(n):
#     if n in [0, 1]:
#         return n
#     return n % 2 + 10 * dec_to_bin(n/2)
# print(dec_to_bin(10))