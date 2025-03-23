'''Given a matirx m, return an array, containing column wise sum'''

def col_wise_sum(matirx):
    n = len(matirx)
    col_sum = []
    m = len(matirx[0])
    for col in range(m):
        sum=0
        for row in range(n):
            sum+=matirx[row][col]
        col_sum.append(sum)
    return col_sum

matirx = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
       ]

print(col_wise_sum(matirx))



