def get_maximum(arr):
    n = len(arr)
    max = float('-inf')
    if n == 1:
        max = arr[0]
    else:
        for num in arr:
            if num>=max:
                max = num
    return max

def get_minimum(arr):
    n = len(arr)
    min = float('inf')
    if n == 1:
        min = arr[0]
    else:
        for num in arr:
            if num<=min:
                min = num
    return min


# arr  = [5,22,29,12,32,69,1,75]
arr = [-5,-22,-29,-12,-32,-69,-1,-75]
# arr = [10,10,10,10,10,10]
# arr = [5,6,7,4,3,1,7]
# arr = [9]
print(get_maximum(arr))
print(get_minimum(arr))

        