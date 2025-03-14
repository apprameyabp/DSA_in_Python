def majorityWins(arr, n, x, y):
        # code here
    count_x = 0
    count_y = 0
    for i in range(n):
        if arr[i] == x:
            count_x += 1
        elif arr[i] == y:
            count_y += 1
        else:
            pass
        
    if count_x>count_y:
        print(count_x,count_y)
        return x

    elif count_y > count_x:
        return y
        
    elif count_x == count_y :
        if x<y:
            return x
        else:
            return y    


arr = [5,22,29,12,32,69,1,75]
n = len(arr)
x = 29 
y = 96
print(majorityWins(arr, n, x, y))