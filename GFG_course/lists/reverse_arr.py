def reverseArray(arr,n):    
    #code here
    for i in range(n//2):
        swap(arr,i,n)
    return arr
    
def swap(arr,i,n):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp

# arr= [1,2,3,4,5,6]
arr = [1,1,2,2,3]
n = len(arr)
print(reverseArray(arr,n))