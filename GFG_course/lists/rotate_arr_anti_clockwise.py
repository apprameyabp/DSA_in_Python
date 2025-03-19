def rotate_arr(arr, k):
    n = len(arr)
    k = k%n
    # print(k)
    # print(n-1)
    # print(n-k)
    # print(k-1)
    #to reverse the complete arr
    reverse(arr,0,n-1)
    print(arr)
    #to reverse the n-k part
    reverse(arr,0,n-k-1)
    print(arr)
    #to reverse k part
    reverse(arr,n-k,n-1)
    return arr

def reverse(arr,start,end):
    for i in range(end):
        if i>=start and i<=end:
            arr[start],arr[end] = arr[end],arr[start] 
            start+=1
            end-=1
    return arr

arr = [1, 2, 3, 4, 5]
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
k = 3

print(rotate_arr(arr,k))