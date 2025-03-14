import math
def prime_factors(number):
    found = False
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            if isPrime(i):
                print(i)            
                found = True
    if not found and isPrime(number):
        print(number)   

def isPrime(number):
    if number==1:
        return False

    for i in range(2, math.floor(math.sqrt(number)+1)):
        if number%i == 0:
            return False

    return True       

number = int(input("Enter a number"))
prime_factors(number)