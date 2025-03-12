def check_equilibrium_index(arr, index):
    n = len(arr)
    ps = [0]*n
    ps[0] = arr[0]
    for i in range(n):
        ps[i] = ps[i-1]+arr[i]
    left_sum = ps[index-1]
    end = n-1
    start = index
    right_sum = ps[end]-ps[start]
    if left_sum==right_sum:
        return True   
    return False
arr = [1,2,3,4,8,4,2,4]
index = 4
print(check_equilibrium_index(arr,index))
    