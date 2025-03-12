arr = [-1,6,3,-10,-4,8,5,-7]
j=len(arr)

# first try : 
# for i in range(j//2):
#     
# print(arr)

# final try : 
def reverse_arr(arr):
    for i in range(j//2):
        swap(arr,i,j)
    print(arr)

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j-i-1]
    arr[j-i-1] = temp

reverse_arr(arr)        

