def factorial(number):
    fact = number
    while number>=2:
        if number == 1 or number == 0:
            fact = 1
        else: 
            fact = fact*(number-1)
            number = number-1
    return fact


number = int(input("Enter the number: "))
print(factorial(number))