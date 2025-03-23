def get_all_subarrays(arr):
    n = len(arr)
    for start in range(n):
        for end in range(start,n):
            for i in range(start,end+1):
                print(arr[i],end = ',')
            print()
    

arr = [1,3,0,-6]
print(get_all_subarrays(arr))