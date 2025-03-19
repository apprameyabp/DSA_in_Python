def immediateSmaller(arr,n,x):
        #return required ans
    arr.sort(reverse = True)
    print(arr)
    second_largest = arr[0]
    for i in range(n-1):
        if x<=arr[i] and x>arr[i+1]:
            second_largest = arr[i+1]
        else:
            pass
    return second_largest

arr = [5,22,29,12,32,69,1,75]
# arr = [4,67,13,12,15]
n = len(arr)
x = 3
print(immediateSmaller(arr,n,x))