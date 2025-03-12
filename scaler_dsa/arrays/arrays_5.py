def reverse_part(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr


def rotate_arr(arr,k):
    n=len(arr)
    k = k%n
    reverse_part(arr,0,n-1)
    reverse_part(arr,0,k-1)
    reverse_part(arr,k,n-1)
    return arr

array = [3,-2,1,4,6,9,8]
rotations = 9
print(rotate_arr(array,rotations))
