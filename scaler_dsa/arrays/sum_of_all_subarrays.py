def total_sum(arr):
    n = len(arr)
    total = 0

    for start in range(n):
        sum=0
        for end in range(start,n):
            sum+=arr[end]
            total+=sum
    return total

arr = [1, 3, 0, -6]
print(total_sum(arr))
