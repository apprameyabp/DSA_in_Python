arr  = [-2,4,6,1,8,5,-10,1]
start = 3
end = 7
n = len(arr)-1 
def reversed_part_arr(arr,start,end):
    for i in range(n):
        if i>=start and i<=end:
            swap(arr,start,end)
            start+=start
            end-=end
        else : 
            pass
    print(arr)
    
def swap(arr,start, end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

reversed_part_arr(arr,start,end)




# first try : 
arr  = [-2,4,6,8,5,-10,-1]
start = 2
end = 4
j = len(arr)-1
for i in range(j):
    if i>=start and i<=end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1
    else:
        pass
print(arr)