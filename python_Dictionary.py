# python Dictionary

# my_dist = {'key': 'sdbghjadb', 'key_2': 'keybjsdbv'}
# print(my_dist)
# my_dst_01 = {} # ()
# print(my_dst_01)
# print(my_dist['key']) # access the element of the distionary

my_dst = {'key': 'assifgdjd', 'key2': 'ksbdkbs'}
my_dst['key'] = 26
my_dst['key3'] = 'UK UL100' 
print(my_dst)


# different methods
# clear()
# copy()
# del my_dst
# fromkeys() 
# new_dst = {}.fromkeys([1,2,3], 0)
# print(new_dst)

# get()

# print(my_dst.get('keyas'))

# items()

print(my_dst.items())

# keys()

print(my_dst.keys())

# popitem()

print(my_dst.popitem())

# setdefault()

print(my_dst.setdefault('key4','added'))

# pop()
print(my_dst.pop('key4', 'not'))

# value()
print(my_dst.values())

# update()
new_D = {'a':'aaa','b':'bbbb', 'c': 'ccc'}
my_dst.update(new_D)
print(my_dst)

# in()

# print(my_dst)

# Amortized case O(n)
# search though the dictionary
# Delete in dictionary

# print(my_dst.pop('key'))
# print(my_dst)
# my_dst.clear()
# print(my_dst)
# time and space complexity 
# def search_key(myDst, value):
#     for key in myDst:
#         if myDst[key] == value:
#             return key, value
#     return 'on thing is permanent'
# print(search_key(my_dst, 24))
# # 
# def trav_fn(dict):

#     for key in my_dst:
#         print(key, my_dst[key])


# trav_fn(my_dst)
# addition in Distionary
# Travers through a dictionary
