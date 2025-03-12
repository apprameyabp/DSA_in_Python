number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# def find_hcf(number1, number2):
#     a = number1
#     b = number2
#     while a!=b:
#         if a>b:
#             a = a-b
#         else:
#             b = b-a
#     return a


# print(find_hcf(number1, number2))


"""Optimized euclidean algorithm"""
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(gcd(number1,number2))