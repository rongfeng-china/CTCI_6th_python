import random
def random_set(v,k):
    result = v[0:k]
    for i in range(k,len(v)):
        index = random.randint(0,i)
        if index < k:
            temp = v[index]
            v[index] = v[i]
            v[i] = temp
    return result

v = [1, 9, 3, 10, 7, 2, 7, 8, 9, 15, 13, -1, -5, -29, 3, -3, 24, 17]
k = 5
result = random_set(v,k)
print result
