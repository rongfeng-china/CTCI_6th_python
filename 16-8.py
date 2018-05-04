dict1 = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
dict2 = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

def english_int(n):
    result = ''
    v0 = n /1000000000000
    v1 = (n-v0*1000000000000) / 1000000000
    v2 = (n -v0*1000000000000- 1000000000 * v1)/1000000
    v3 = (n-v0*1000000000000- 1000000000*v1 - 1000000*v2)/1000
    v4 = n-v0*1000000000000  -1000000000*v1 - 1000000*v2 - 1000*v3

    if v0 != 0:
        result += convert(v0) + ' trillion '
        if (v1 == 0 and (v2 !=0 or v3!=0 or v4!=0)) or (v1 != 0 and v2 == 0 and v3 == 0 and v4 == 0):
            result += 'and ' 
    if v1 != 0:
        result += convert(v1) + ' billion '
        if (v2 == 0 and (v3!=0 or v4!=0)) or (v2 != 0 and v3 ==0 and v4 == 0):
            result += 'and '
    if v2 != 0:
        result += convert(v2) + ' million '
        if v3 ==0 and v4 !=0:
            result += 'and '
    if v3 != 0:
        result +=  convert(v3) + ' thousand '
        if v4 != 0:
            result += 'and '
    if v4 != 0:
        result += convert(v4)  
    if v1 ==0 and v2 == 0 and v3 == 0 and v4 == 0:
        result = "zero"
    return result

def convert(n):
    if n >= 1000:
        print 'error'
    v1 = n/100
    result = ''
    v2 = (n-v1*100)/10
    v3 = n - v1* 100 - v2*10
    
    if v1 != 0:
        #print n
        #print v1
        #print dict1[v1]
        result = dict1[v1] + " hundred"
        if v2 != 0 or v3 != 0:
            result += " and "
    
    if v2 == 1:
        result += dict1[v2*10+v3]
    else:
        if v2 != 0:
            result += dict2[v2*10]
        if v3 != 0:
            result += " " + dict1[v3] 
    return result
             
result = english_int(0)
print result

result = english_int(1)
print result

result = english_int(8)
print result

result = english_int(15)
print result

result = english_int(92)
print result

result = english_int(113)
print result

result = english_int(1001)
print result

result = english_int(2075)
print result

result = english_int(20066)
print result

result = english_int(500012)
print result

result = english_int(95000)
print result

result = english_int(1000000)
print result

result = english_int(6000000)
print result

result = english_int(2006000001)
print result

result = english_int(6020000000)
print result

result = english_int(3000000000042)
print result
