'''Given a matrix M, return an array containing the column wise max'''
def col_wise_max(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col_max_arr = []
    for col in range(m):
        col_max = -float('inf')
        for row in range(n):
            if matrix[row][col]>=col_max:
                col_max = matrix[row][col]
        col_max_arr.append(col_max)
            
    return col_max_arr


matirx = [
    [-1,2,3], 
    [-1,5,-6], 
    [-1,8,-9]
       ]

print(col_wise_max(matirx))