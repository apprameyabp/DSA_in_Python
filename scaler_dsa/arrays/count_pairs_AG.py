def count_pairs(string1):
    n = len(string1)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            char1 = string1[i]
            char2 = string1[j]
            if char1 == 'a' and char2 == 'g':
                print(i,j)
                count+=1
            else:
                pass
    print(count)
string1 = 'kliouggggaaaabbbbc'
count_pairs(string1)
