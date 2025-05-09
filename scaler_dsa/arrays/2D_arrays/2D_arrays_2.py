"""Given a 2D array m, print the kth element in rth row"""

def print_row_element(m,r,k):
        print(m[r][k])


matirx = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
       ]

r = 1
k = 2

print_row_element(matirx,r,k)