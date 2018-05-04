def subtract(a,b):
    return a+(-b)

def multiply(a,b):
    c = abs(b)
    result = 0
    for i in range(c):
        result += a
    if b>=0:
        return result
    else:
        return -result


def division(a,b):
    if b == 0:
        return None
    a1,b1 = abs(a),abs(b)
    result = 0

    while a1 >= b1:
        a1 -= b1
        result += 1

    if int(a>0)+int(b>0) == 1:
        return -result
    return result



result = multiply(3, 6)
print result

result = multiply(7,11)
print result

result = multiply(-8, 10)
print result

result = division(3,6)
print result

result = division(30, 6)
print result

result = division(34,-6)
print result
    
result = division(120, 10)
print result

result = subtract(34, 6)
print result

result = subtract(31, -6)
print result
