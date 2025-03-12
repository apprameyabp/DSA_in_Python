arr  = [2,5,7,-1,6,-4]
k=1
n = len(arr)
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] + arr[j] == k:
            print('{},{}'.format(arr[i],arr[j]))


