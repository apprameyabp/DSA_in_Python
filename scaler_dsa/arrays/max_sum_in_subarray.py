def max_sum_in_subarray(arr):
    n = len(arr)
    max_sum = -float('inf')
    for start in range(n):
        sum = 0
        for end in range(start,n):
            sum+=arr[end]
            if sum>=max_sum:
                max_sum = sum
    return max_sum            

arr = [1, 3, 0, -6,]
print(max_sum_in_subarray(arr))