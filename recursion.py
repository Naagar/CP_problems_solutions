
import numpy as np
two_dim_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_dim_arr)
new_twoD_arr = np.array(two_dim_arr, 1, [[1,2,3]], axis=1)
# from array import *

# # 2D arrays
# two_dim_arr = [[1,10],[2,3]]
# print(two_dim_arr)
# arr_01 = array('i',[1,2,3,4,5,6])
# arr_01.remove(4) # input is value not index
# arr_01.append(6)
# arr_01.append(6)
# arr_01.append(6)
# arr_01.extend(arr_01) # arr_01 + arr_01
# print(arr_01) 
# list_temp = [1,2,3,4]
# arr_01.fromlist(list_temp) # add list to the end of arrar
# print(arr_01)
# # print(buffer_info(arr_01))
# print(arr_01.buffer_info())  # print the info of array size, and filled size
# print(arr_01.count(2)) # count the no of occurance of an element(value)
# temp_str = arr_01.tostring()
# print(temp_str)
# # arr_01.tolist() . # array to list
# arr_01.fromstring(temp_str) # add string to the array
# arr_01[1:4] # access value from an index to other next index / slicing
# Location of element in an array
# def find_el(array, el):
#     for i in array:
#         # print(i)
#         if i == el:
#             return arr_01.index(el)
    
#     return 'element does not exist in array'
# print(find_el(arr_01,6))
# Array traversal
# my_array = 
# def travers(array):
#     for i in array:
#         print(array[i-1])


# travers(arr_01)
# def accessElement(array, index):
#     if index >= len(array):
#         print('out of index ')
#     else:
#         print(array[index])
# accessElement(arr_01, 4)
# arr_01.insert(5,7) # index, values
# print(arr_01)
# # arr_02 = array('d', [1,2,3,4,5,6,7])
# arr_02 = [2.3,4,5,6,7]
# print(arr_01)
# print(arr_02[0])

# sys.setrecursionlimit(10000000)

# def decimal_to_bin(n):
#     assert int(n) == n, 'number must be an integer!'
#     if n == 0:
#         return 0
#     else:
#         return n % 2 + 10 * decimal_to_bin(int(n/2))
# print(decimal_to_bin(1000))
# # Euclidian algo for GCD
# def gcd(n, m):
#     assert int(n) == n and int(m) == m , 'assert error number must be an integer'
#     if n < 0:
#         n = -1 * n
#     if m< 0:
#         m = -1 * m
#     if m == 0:
#         return n
#     else:
#         return gcd(m, n % m)
# print(gcd(10000000000000000000000000,     18))
# def power_fun(n,exp):
#     assert n >= 0 and int(exp) >= 0, 'number exp is not non positive'
#     if exp == 1:
#         return n
#     elif exp == 0:
#         return 1
#     else:
#         return n * power_fun(n,exp-1)
# print(power_fun(1222222, 22))
# def fun_sum_digit(n):
#     assert n>=0 and int(n) == n, 'assert error, no is '
#     if n == 0 :
#         return n
#     else:
#         return fun_sum_digit(int(n/10)) + int(n % 10)
# a = fun_sum_digit(12346)
# print(a)
# def fn_num_fun(n):
#     assert n>= 0 and int(n) == n, 'number should be posative'
#     if n in [0,1]:
#         return n
#     else:
#         return fn_num_fun(n-1) + fn_num_fun(n-2)
# fb_num = fn_num_fun(40)
# print(fb_num)
# def rec_fun(n):
#     if n < 1:
#         return n
#     else: 
#         return n + rec_fun(n-1)
# def rec_fun_1(n):
#     if n <= 0 and int(n) == n : # The Number must be shoud be positive integer 
#         return 1
#     else:
#         return n * rec_fun_1(n-1)
# n = input("enter no.:")
# n = int(n)
