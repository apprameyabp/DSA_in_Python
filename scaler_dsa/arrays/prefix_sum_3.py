def check_odd_even_sum(arr,queries):
    # print(arr)
    n = len(arr)
    ps_even = [0]*n
    ps_odd = [0]*n
    for i in range(1,n):
        ps_even[0]=arr[0]
        if i%2 == 0:     
            ps_even[i] = ps_even[i-1] + arr[i]
        else:
            ps_even[i] = ps_even[i-1]

    for i in range(1,n):
        if i%2 != 0:
            ps_odd[i] = ps_odd[i-1] + arr[i]
        else:
            ps_odd[i] = ps_odd[i-1]

    for i in range(queries):
        start = int(input("enter the start index: "))
        end = int(input("Enter the end index: "))
        even_odd = input("Enter 'E' for even and 'O' for odd: ").lower()
        if even_odd == 'e':
            if start == 0:
                sum = (ps_even[end])
            else:
                # print("start: ",ps_even[start-1] , " " ,  "end: ", ps_even[end] )
                sum = ps_even[end] - ps_even[start-1]
        elif even_odd == 'o':
            if start == 0:
                sum = (ps_odd[end])
            else:
                sum = ps_odd[end] - ps_odd[start-1]
        else:
            print('Invalid input')
        print(sum)


    # print(ps_even)
    # print(ps_odd)

arr = [2,3,1,-1,0,8,5,4]
queries = int(input("enter the number of queries: "))
check_odd_even_sum(arr,queries)