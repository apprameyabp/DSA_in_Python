import math
def find_max_distance(arr):
    # Write your code here
    n=len(arr)
    total_sum = sum(arr)
    avg = total_sum//n
    indices=[]
    for i in range(n):
        if arr[i] == avg:
            indices.append(i)
    
    if len(indices)<=2:
        max_distance = -1
    else:
        max_distance = indices[len(indices)-1] - indices[0]
    
    return max_distance

N = input()
arr = list(map(int, input().split()))
print(find_max_distance(arr))