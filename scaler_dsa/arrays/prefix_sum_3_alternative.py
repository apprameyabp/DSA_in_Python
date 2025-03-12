def check_even_sum(arr):
    n = len(arr)
    ps_even = [0]*n
    ps_odd = [0]*n
    ps_even[0] = arr[0]
    for i in range(n):
        if i%2 == 0:            
            ps_even[i] = ps_even[i-1]+arr[i]
        else:
            pass
    print(ps_even)
    print(ps_odd)

arr = [2,3,1,-1,0,8,5,4]

check_even_sum(arr)