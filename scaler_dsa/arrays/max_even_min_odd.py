"""Given an array of length N, find the max even and min odd in the array"""


def max_even_min_odd(arr):
    n = len(arr)
    max_even = None
    min_odd = None
    for i in range(n-1, -1, -1):
        if arr[i] % 2 == 0:
            if arr[i]>max_even :
                max_even = arr[i]
                # max_even_ans = max(ans,)
        elif arr[i] % 2 != 0:
            if arr[i] < min_odd :
                min_odd = arr[i]
        else:
            pass
    return max_even , min_odd

arr = [10,1,8,87,92,101,1,67,78]

print(max_even_min_odd(arr))