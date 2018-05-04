def count2s(n):
    n_str = str(n)
    bits = len(n_str)
    result = 0
    ## highest
    if int(n_str[0]) > 2:
        result += 10**(bits-1)
    else:
        if int(n_str[0]) == 2:
            result += (n-(10**(bits-1))*2)+1
    
    for i in range(1,bits):
        result += 10**(bits-1-i)*int(n_str[:i])
        if int(n_str[i]) > 2:
            result += 10**(bits-1-i)
        else:
            if int(n_str[i]) == 2:
                if i == bits-1:
                    result += 1
                else:
                    result += (int(n_str[i+1:])+1)
    return result
       
n = 100
result = count2s(n)
print result

n = 22
result = count2s(n)
print result

n = 329715
result = count2s(n)
print result
