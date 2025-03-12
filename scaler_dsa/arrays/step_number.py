def find_one_step_numbers(start,end):
    #Write your logic here
    n = end+1
    for num in range(start,n):
        digit_list= [int(digit) for digit in str(num)]
        for i in range(len(digit_list)-1):
            step_diff = abs(digit_list[i+1] - digit_list[i])
            if diff == 1:
                print(num)
    print('-1')

    

start = int(input())
end = int(input())
print(find_one_step_numbers(start , end ))
