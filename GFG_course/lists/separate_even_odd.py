def separate_even_odd(arr):
    even = []
    odd =[]
    even = [num  for num in arr if num%2 == 0]
    odd = [num for num in arr if num%2 !=0]
    return even, odd

arr = [22,17,21,19,14,88,65,42]
print(separate_even_odd(arr))