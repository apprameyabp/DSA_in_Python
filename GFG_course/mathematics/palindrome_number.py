def check_palindrome_number(number):
    reversed = reversed_number(number)
    if reversed == number:
        return True
    return False
def reversed_number(number):
    sum = 0
    while(number>0):
        rem = number%10
        sum = sum*10+rem
        number=number//10
    return sum


number = int(input("Enter the end number: "))
print(check_palindrome_number(number))
