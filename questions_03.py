# 
# import numpy as np
# import matplotlib.pyplot as plt

# x_coords = np.linspace(-200, 200, 600)
# y_coords = np.linspace(-200, 200, 600)
# heart_x = []
# heart_y = []
# for y in y_coords:
#     for x in x_coords:
#         if ((x*0.01)**2+(y*0.01)**2-1)**3-(x*0.01)**2*(y*0.01)**3 <= 0:
#             heart_x.append(x)
#             heart_y.append(y)
            
# plt.scatter(heart_x, heart_y, c="pink")
# plt.axis('off')
# plt.show()
strs1 = ["flower","flow","flight"]
print(zip(*strs1))
def longestCommonPrefix(strs):
    pre = ''
    for i in zip(*strs):
        if len(set(i)) == 1:
            pre +=i[0]
            print(pre)
        else:
            break
    return pre
longestCommonPrefix(strs1)

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]
 
# using zip() to map values
mapped = zip(name)
 
# converting values to print as list
mapped = list(mapped)
 
# printing resultant values
print("The zipped result is : ", end="")
print(mapped)
 
print("\n")
 
# unzipping values
# namz, roll_noz, marksz = zip(*mapped)
 
# print("The unzipped result: \n", end="")
 
# # printing initial lists
# print("The name list is : ", end="")
# print(namz)
 
# print("The roll_no list is : ", end="")
# print(roll_noz)
 
# print("The marks list is : ", end="")
# print(marksz)