def rotate(arr,k):
    n = len(arr)
    k = k%n
    reverse(arr,k,n-1)
    reverse(arr,0,k-1)
    reverse(arr,0,n-1)

    return arr


def reverse(arr,start,end):
    for i in range(end+1):
        if i>=start and i<=end:
            arr[start],arr[end] = arr[end], arr[start]
            start+=1
            end-=1
    return arr

arr=[18,12,9,8,-4,3]
print(rotate(arr,3))
        
         

