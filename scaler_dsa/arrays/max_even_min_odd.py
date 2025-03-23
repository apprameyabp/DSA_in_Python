"""Given an array of length N, find the max even and min odd in the array"""


def max_even_min_odd(arr):
    n = len(arr)
    max_even = None
    min_odd = None
    for num in arr:
        if num % 2 == 0:
            if max_even is None or num>max_even:
                max_even = num
        else:
            if min_odd is None or num<min_odd:
                min_odd = num
    return max_even , min_odd

arr = [10,-1,8,87,-92,101,1,-67,78]
arr = [-1,-2,-3,-4,-5,-6,-7]
print(max_even_min_odd(arr))