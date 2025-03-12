def check_pair(string1):
    n = len(string1)
    g_count = 0
    pair_count = 0
    for i in range(n-1,-1,-1):
        if string1[i].lower() == 'g':
            g_count +=1
        elif string1[i].lower() == 'a':
            pair_count +=g_count
        else:
            pass
 
    print(pair_count)


string1 = 'ggggaaavf'
check_pair(string1)


