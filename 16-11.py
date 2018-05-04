def diving_board(k, short, long):
    if short == long:
        return k*short
    result = []
    for i in range(k+1):
        result.append(i*short+(k-i)*long)
    return result



k, short, long = 5,3,4
result = diving_board(k,short,long)
print result

k, short, long = 4,2,6
result = diving_board(k,short,long)
print result
