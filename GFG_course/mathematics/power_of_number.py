def power(x,n):
    if n == 0:
        return 1
    temp = power(n//2)
    