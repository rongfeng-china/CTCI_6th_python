def cal(a,b):
    result = a^b
    carry = (a&b) << 1
    return result + carry

a = 13
b = 924
result = cal(a,b)
print result

