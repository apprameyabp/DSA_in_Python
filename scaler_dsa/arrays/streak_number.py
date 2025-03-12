def validate_number(input_number): 
    num_arr = list(map(int,str(input_number)))
    n = len(num_arr)
    order=0
    sum_E=0
    for i in range(n):
        if i%2 ==0:
            o_2 = num_arr[i] * 2
            if o_2<len(num_arr):
                order = o_2
        else:
            sum_E+=num_arr[i]
        
    sum_streak = order+sum_E
    k=0
    while (sum_streak+k)%(k+1)==0:
        k+=1
    print(k)
input_number = int(input())
validate_number(input_number)    

