'''Find the smallest sub-array which contains both the max and min of the array'''

def smallest_subarray(arr):
    n = len(arr)
    max_arr = max(arr)
    min_arr = min(arr)
    print('max_arr: ', max_arr)
    print('min_arr: ', min_arr)
    max_index = None
    min_index = None
    len_sub_array = 0
    ans = n
    for i in range(n-1,-1,-1):
        len_sub_array = (abs(max_index - min_index)) + 1
        if arr[i] == max_arr:
            max_index = i
            if min_index != None:
                len_sub_array = (abs(max_index - min_index)) + 1
                ans = min(ans,len_sub_array)
        elif arr[i] == min_arr:
            min_index = i
            if max_index != None:
                len_sub_array = (abs(max_index - min_index)) + 1
                ans = min(ans,len_sub_array)
        else: 
            pass
    print('final_ans ', ans)


arr= [1,6,4,2,7,5,3,1,1,5]
smallest_subarray(arr)


