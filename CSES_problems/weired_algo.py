# weired_algo.py

def weired_algo(n):
    while n is not 1:
        if n % 2 == 0:
            n = n/2
            print(n)
        else:
            n = n * 3 + 1
            print(n)
    return 
def missing_no(arr):
    n = len(arr) + 1
    sum_nums = (n * (n-1)) / 2
    sum_temp =sum(arr)
    number= sum_nums - sum_temp
    return number
def dna(seq):
    s = []
    sub_A = []
    for i in range(len(seq)):
        if seq[i] == 'A' and seq[i-1] == 'A':
          sub_A.append('A')

def increasing_array(arr, n):
    temp = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = temp + (arr[i]- arr[i+1])
    return temp

def cut_paste(arr, n_ops):

    for i in range(n_ops):
        
        temp = arr[n_ops[i][0]:n_ops[i][1]]
        right = arr[n_ops[i][1]:]
        arr = arr[:n_ops[i][0]-1]
        arr.append(right)
        arr.append(temp)


