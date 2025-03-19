def find_smaller_elements(arr,x):
    for num in arr:
        if num<x:
            print(num, end=" ")
    print()
    
arr = [8, 100, 20, 40, 3, 7]
x = 10

find_smaller_elements(arr,x)
