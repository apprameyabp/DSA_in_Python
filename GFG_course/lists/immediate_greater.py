def immediate_greater(arr,x):
    greater = max(arr)
    next_greater = None

    for num in arr:
        if num<=greater or num is not None:
                next_greater = num
                if next_greater<greater:
                    next_greater = num
                elif next_greater == greater:
                     next_greater = num
    return next_greater

arr = [4,67,13,12,15]
x = 16

print(immediate_greater(arr,x))



         
