def find_odd_even_sum(arr,queries,):
    n = len(arr)
    even_indices = (n+1)//2
    odd_indices = (n)//2
    ps_even = [0]*even_indices
    ps_odd = [0]*odd_indices
    for i in range(n):
        if i%2 == 0:
            if i == 0:
                ps_even[0] = arr[0]
            else:
                ps_even[i] = ps_even[i] + arr[i+2]
        else:
            if i == 1:
                ps_odd[0] = arr[1]
            else :
                ps_odd[i] = ps_odd[i-1] + arr[i+2]

    print(ps_even)
    print(ps_odd)
    for q in range(q):
        start = int(input("enter the start index: "))
        end = int(input("Enter the end index: "))
        odd_even = input("Enter 'O' for odd and 'E' or even").lower()
        if odd_even == 'e':
            if start == 0:
                sum=ps_even[start]
                

arr = [2,3,1,-1,0,8,5,4]
find_odd_even_sum(arr,4)