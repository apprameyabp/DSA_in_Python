def sum_of_each_subarray(arr):
    n = len(arr)
    for start in range(n):
        sum = 0
        for end in range(start,n):
            sum+=arr[end]
            print('Sum of {}:{} is {}'.format(start,end,sum))            

arr = [1, 3, 0, -6,]
sum_of_each_subarray(arr)