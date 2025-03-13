def leaders_in_array(arr):
    n = len(arr)
    count = 1
    max = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i]>max:
            count+=1
            max = arr[i]
        else : pass
    return count

arr = [8, -2, 4, 7, 6, 5, 1]
arr = [1011,808,8,111,13]

print(leaders_in_array(arr))

        