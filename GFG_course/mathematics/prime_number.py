def isPrime(number):
    if number == 2 or number == 3:
        return True
    elif number %2 == 0 or number %3 == 0:
        return False
    else:
        i=5
        while(i*i <=number):
            if(number%5 == 0 and number % (i+2) == 0):
                return False
            i+=6
    return True

