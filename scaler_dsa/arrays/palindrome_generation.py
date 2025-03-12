input_word = input()

def reverse_check(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end=-1
    return arr

def palindrome_check(input_word):
    arr = list(input_word)
    n=len(arr)
    k=0
    while k<=n:
        reverse_check(arr,0,n-1)
        reverse_check(arr,0,k-1)
        reverse_check(arr,k,n-1)
        k+=1
    arr_str = ''.join(str(x) for x in arr)
    rev_str = arr_str[::-1]
    if arr_str==rev_str: return True
    else : return False


input_word = input()
print(palindrome_check(input_word))




