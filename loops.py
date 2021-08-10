#1
from functions_basic2 import nums


def big(nums_list):
    for i in range(len(nums_list)):
        if nums_list[i] > 0:
            nums_list[i] = "big"
    return nums_list

print(big([1,-2,9,-4,-1,9]))

#2
def positive(nums_list):
    counter = 0
    for i in range(len(nums_list)):
        if nums_list[i] > 0:
            counter +=1
    last = len(nums_list)-1
    nums_list[last] = counter
    return nums_list
print(positive([1,2,4,2,23]))

#3
def total(nums_list):
    sum = 0
    for i in range(len(nums_list)):
        sum = sum + nums_list[i]
    return sum
print(total([1,2,3]))

#4
def average(nums_list):
    avg = 0
    sum = 0
    for i in range(len(nums_list)):
        sum = sum + nums_list[i]
        avg = sum / len(nums_list)
    return avg
print(average([1,2,3,4,5,6]))

#5
def lengthy(nums_list):
    return len(nums_list)
print(lengthy([1,2]))

#6
def minimum(nums_list):
    if len(nums_list) == 0:
        return False
    else:
        min = nums_list[0]
        for i in range(len(nums_list)):
            if nums_list[i] < min:
                min = nums_list[i]
        return min

print(minimum([1,5,4,3,9,7,-1,6]))
print(minimum([]))

#7
def maximum(nums_list):
    if len(nums_list) == 0:
        return False
    else:
        max = nums_list[0]
        for i in range(len(nums_list)):
            if nums_list[i] > max:
                max = nums_list[i]
        return max    

print(maximum([1,5,4,3,9,7,-1,6]))
print(maximum([]))

#8
def ultimate(nums_list):
    sum =total(nums_list)
    avg = average(nums_list)
    min = minimum(nums_list)
    max = maximum(nums_list)
    len = lengthy(nums_list)
    analysis = {
        'total' : sum,
        'average' : avg,
        'minimum' : min,
        'maximum' : max,
        'length' : len,
    }
    return analysis
print(ultimate([1,5,4,3,9,7,-1,6]))

#9
def reverse(nums_list):
    list_len = len(nums_list)
    for i in range(int(list_len/2)):
        temp = nums_list[list_len-1-i]
        nums_list[list_len-1-i] = nums_list[i]
        nums_list[i] = temp
    return nums_list

print(reverse([3,1,8,10,-5,6]))