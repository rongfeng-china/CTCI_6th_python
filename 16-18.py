def matches_pattern(string, format):
    print '%s %s' %(string, format)
    n1,n2 = len(string),len(format)
    if n1 == 0 or n2 == 0:
        return False

    a_count,b_count = 0,0
    for letter in format:
        if letter == 'a':
            a_count += 1
        else:
            b_count += 1
    
    if b_count == 0:
        a_len = 1.0*n1/a_count
        if a_len != int(a_len):
            return False
        else:
            return check(string,int(a_len),0,format)
    if a_count == 0:
        b_len = 1.0*n1/b_count
        if b_len != int(b_len):
            return False
        else:
            return check(string,0,int(b_len),format)

    for a_len in range(1,int(n1/a_count)+1):
        b_len = 1.0*(n1-a_len * a_count)/b_count     
        if b_len == int(b_len):
           re = check(string,a_len,int(b_len),format)
           if re:
               return True
    return False


def check(string, a_len, b_len, format):
    a_letter,b_letter = '',''
    start_index,end_index = 0, -1

    for index in range(0,len(format)):
        if end_index == -1:
            if format[index] == 'a':
                end_index = a_len-1
                a_letter = string[start_index:end_index+1]
            else:
                end_index = b_len-1
                b_letter = string[start_index:end_index+1]
        else:
            if format[index] == 'a':
                start_index = end_index+1
                end_index = start_index + a_len-1
                a_tmp = string[start_index:end_index+1]
                if a_letter == '':
                    a_letter = a_tmp
                else:
                    if a_letter != a_tmp:
                        return False
            else:
                start_index = end_index+1
                end_index = start_index + b_len-1    
                b_tmp = string[start_index: end_index+1]
                if b_letter == '':
                    b_letter = b_tmp
                else:
                    if b_letter != b_tmp:
                        return False
    return True


result = matches_pattern("dogdogturtledog", "aaba")
print result
result = matches_pattern("dogdogturtledog", "bbab")
print result
result =matches_pattern("dogdogturtledogdog", "aabaa")
print result
result = matches_pattern("dogdogturtledogdog", "aba")
print result
result = matches_pattern("dogdogturtledogdo", "aba")
print result
result = matches_pattern("catcatbirdbird", "aabb")
print result
result = matches_pattern("buffalobuffalobuffalobuffalo", "aaaa")
print result
result = matches_pattern("dogdogturtledogdg", "aba")
print result
result = matches_pattern("catcatcatbirdbird", "aabb")
print result
result = matches_pattern("buffalobuffalouffalobuffalo", "aaaa")
print result

