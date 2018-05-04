def swapper(a,b):
    a ^= b
    b ^= a
    a ^= b
    return a,b    

a = 12345
b = 10101
a,b = swapper(a,b)
print a,b

