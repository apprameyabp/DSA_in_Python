def check_equilibrium_index(arr):
    n = len(arr)
    ps = [0]*n
    ps[0] = arr[0]
    for i in range(n):
        ps[i] = ps[i-1]+arr[i]
    print('ps: ', ps )
    
    for index in range(n):
        print('index: ', index)
        if index == 0:
            left_sum = 0
            right_sum = ps[n-1]
            print("left_sum: ", left_sum)
            print("right_sum: ", right_sum)
            if check_sum(left_sum,right_sum):
                print(index)
            
        elif index == n-1:
            left_sum = ps[n-1]
            right_sum= 0
            print("left_sum: ", left_sum)
            print("right_sum: ", right_sum)
            if check_sum(left_sum,right_sum):
                print(index)
            
        # elif index>0 and index<n-1: 
        else:
            left_sum = ps[index-1]
            end = n-1
            start = index
            # print('start: ', start)
            right_sum = ps[end]-ps[start]
            print("left_sum: ", left_sum)
            print("right_sum: ", right_sum)
            if check_sum(left_sum,right_sum):
                print(index)

    print("-1")

arr = [1,2,3,4,8,4,2,4]
def check_sum(left_sum,right_sum):
    if left_sum == right_sum:
        return True
check_equilibrium_index(arr)
    