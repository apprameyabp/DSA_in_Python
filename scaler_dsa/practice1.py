arr = [3,-2,1,4,6,9,8]
k = 3

def reverse_k(arr,k):
    n = len(arr)-1
    start = len(arr)-k
    end = n
    for i in range(n-k,n):
        if(i>start and i<=end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start+=1
            end-=1
            print(arr)
        else:
            pass
    return arr

def reverse_n_k(arr=arr,k=k):
    arr = reverse_k(arr=arr,k=k)
    n= len(arr)-1
    start=0
    end=n-k
    print('end',end)
    for i in range(end):
        if i>=start and i<=end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start+=1
            end-=1
        else:
            pass
    return arr

arr = reverse_n_k(arr,k)
print(arr)