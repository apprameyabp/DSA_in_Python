# import math
# def sum_natural_number(n):
#     num=1
#     sum=0
#     # range = math.ceil(n/2)
#     # print(range)
#     while num <= n :
#         sum+=num
#         num+=1
#     # sum = sum*2    
#     print(sum)

# sum_natural_number(5)        


number = int(input("Enter the end number: "))
def natural_number(n):
    return n*((n+1)//2)

print(natural_number(number))