# Problem statement : 
# given the array of length N, find how many elements have at least one element greater than themselves. 

# method 1 : using max() and count() for small and medium lists
list = [56,112,90,45,76,13,15, 45,89,112,89,56,45,13]
max_ele = max(list)
count_of_max_ele = list.count(max_ele)
ele_greater = len(list) - count_of_max_ele
print(ele_greater)


#method 2 : 



def count_of_max_value(list1):
    max_value = float('-inf')
    count_of_max_value = 0
    for num in list1 : 
        if num > max_value:
            max_value = num
            count_of_max_value = 1
        elif num == max_value:
            count_of_max_value+=1   
    return count_of_max_value
list1 = [56,112,90,45,76,13,15, 45,89,112,89,56,45,13]
count_of_ele = len(list1) - count_of_max_value(list1)
print(count_of_ele)

arr = [5, 3, 8, 2, 8, 7, 8]

max_val = float('-inf')  # Smallest possible value
count_max = 0

for num in arr:
    if num > max_val:
        max_val = num  # Update max value
        count_max = 1  # Reset count since we found a new max
    elif num == max_val:
        count_max += 1  # Increment count if it's equal to max

print(f"Maximum element: {max_val}, Count: {count_max}")