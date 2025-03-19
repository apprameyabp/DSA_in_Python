def is_sorted_list(arr):
    n = len(arr)
    inc_flag = False
    dec_flag = False
    if n == 1 or n == 0:
        inc_flag = True    
    else: 
        for i in range(n-1):    
            if arr[i+1] >= arr[i]:
                inc_flag = True
            else :
                inc_flag = False
                break
        for i in range(n-1):
            if arr[i+1]<=arr[i]:
                dec_flag = True
            else:
                dec_flag = False
                break        
    return inc_flag or dec_flag
arr = [11,11,10,10,10,10,10,10]
# arr = [5,22,29,12,32,69,1,75]
# arr = [45,34,23,11,9,-1,-23]
# arr = [-5,-22,-29,-12,-29,-32,-69,-1,-75]
# arr = []
print(is_sorted_list(arr))