def count_digits(number):
    digit_count=0
    while number>0:
        digit_count += 1
        number = number//10
    print(digit_count)
    
number = int(input("Enter the number: "))
count_digits(number)

