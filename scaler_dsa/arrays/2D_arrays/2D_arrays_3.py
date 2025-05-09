'''Given a matirx m, return an array, containing row wise sum'''

def row_wise_sum(matirx):
    n = len(matirx)
    sum_arr = []
    m = len(matirx[0])
    for row in range(n):
        sum=0
        for col in range(m):
            sum+=matirx[row][col]
        sum_arr.append(sum)
    return sum_arr

matirx = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
       ]

print(row_wise_sum(matirx))



