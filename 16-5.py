def factorial_zero(n):
    result = 0
    while n > 4:
        n = n/5
        result += n
    return result



result = factorial_zero(4)
print result

result = factorial_zero(9)
print result

result = factorial_zero(10)
print result

result = factorial_zero(25)
print result

result = factorial_zero(55)
print result
