def getKthMagicNumber(k):
    v = 1
    if k == 1:
        return v
    else:    
        Q3,Q5,Q7 = [3],[5],[7]
        for time in range(2,k+1):
            min_v = Q3[0]
            min_index = 3
            if Q5[0] < min_v:
                min_v = Q5[0]
                min_index = 5
            if Q7[0] < min_v:
                min_v = Q7[0]
                min_index = 7

            if min_index == 3:
                v = Q3.pop(0)
                Q3.append(v*3)
                Q5.append(v*5)
                Q7.append(v*7)
                
            elif min_index == 5:
                v = Q5.pop(0)
                Q5.append(v*5)
                Q7.append(v*7)
             
            else:
                v = Q7.pop(0)
                Q7.append(v*7)
    return v


result = getKthMagicNumber(38)
print result
            
result = getKthMagicNumber(653)
print result   


