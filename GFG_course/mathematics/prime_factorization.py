import math
def prime_factors(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            if isPrime(i):
                print(i)            
                # print(number)
        
def isPrime(number):
    if number==1:
        return False
    prime = True

    for i in range(2, math.floor(math.sqrt(number)+1)):
        if number%i == 0:
            prime = False
            break
    return prime       

number = 13
prime_factors(number)