def all_divisors(number):    
    i=1
    while (i*i <=number):
        if number%i == 0:
            print(i)
            divisor = number//i
            if i != divisor:
                print(divisor)
        i+=1
number = int(input('Enter the number: '))
all_divisors(number)
