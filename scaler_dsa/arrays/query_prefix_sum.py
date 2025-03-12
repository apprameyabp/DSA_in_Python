def query_sum(arr,query):
    n = len(arr)
    prefix_sum = [0]*n
    prefix_sum[0] = arr[0]
    for i in range(1,n):
        prefix_sum[i]=prefix_sum[i-1] + arr[i]
    print(prefix_sum)
    for i in range(query):
        start = int(input("enter the start index: "))
        end = int(input("Enter the end index: "))
        if start == 0:
            sum = (prefix_sum[end])
        else:
            print("start: ",prefix_sum[start-1] , " " ,  "end: ", prefix_sum[end] )

            sum = prefix_sum[end] - prefix_sum[start-1]
        print(sum)

arr= [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
query = int(input("enter the number of queries: "))
query_sum(arr,query)
        