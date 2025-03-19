def find_second_largest(arr):
    max_arr = max(arr)
    second_largest = float('-inf')
    if len(arr)<=1:
            return None
    for num in arr:
        if num<max_arr and num>second_largest:
            second_largest = num                 
            # second_largest = max(second_largest,num)

    return second_largest

# arr = [5,22,29,12,32,69,1,75]
arr = [1]
# arr = [-5,-22,-29,-12,-32,-69,-1,-75]
print(find_second_largest(arr))

        
        