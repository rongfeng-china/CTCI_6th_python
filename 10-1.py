def sorted_merge(a,b):
    n1,n2 = len(a),len(b)
    index_a = n1-n2-1
    index_b = n2-1
    index_merged = n1-1
    while  index_merged>0:
        if index_a == -1:
           a[0:1+index_merged]=b[0:1+index_merged]
           break
        if index_b == -1:
           break
        if a[index_a] > b[index_b]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1
    return a

a = [33, 44, 55, 66, 88, 99, None, None, None]
b = [11, 22, 77]
print sorted_merge(a,b)

a = [11, 22, 55, 66, 88, None, None, None]
b = [33, 44, 99]
print sorted_merge(a,b)

