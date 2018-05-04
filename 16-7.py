def number_max(a,b):
    val = b-a
    sign = (val & (1<<63))>>63
    result = sign * a + (1-sign) * b

    return result


result = number_max(10000,10)
print result

result = number_max(0x10000,0xFFFF)
print result

result = number_max(1212121,1234567)
print result
