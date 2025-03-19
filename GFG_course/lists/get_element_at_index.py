def get_element(arr,index):
    n = len(arr)
    if index >= n:
        return -1
    else:
        return arr[index]

arr = [5,22,29,12,32,69,1,75]
print(get_element(arr,7))