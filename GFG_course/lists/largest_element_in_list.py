def largest_element(arr):
    max = float('-inf')
    for num in arr:
        if num>max:
            max = num
        elif len(arr) == 0:
            return None
    return max

# arr = [-5,-22,-29,-12,-32,-69,-1,-75]
arr = [5,22,29,12,32,69,1,75]
print(largest_element(arr))
