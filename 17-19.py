import math
def oneMissing(arr):
    n = len(arr)+1
    exp_sum = n*(n+1)/2
    return exp_sum - sum(arr)

def twoMissing(arr):
    n = len(arr)+2
    exp_sum = n*(n+1)/2
    exp_product = 1
    for i in range(1,n+1):
        exp_product *= i
   
    real_sum,real_product = 0,1
    for num in arr:
        real_sum += num
        real_product *= num

    v1 = exp_sum - real_sum  # a+b
    v2 = exp_product / real_product  # a*b

    a = (v1-math.sqrt(v1**2-4*v2))/2
    b = v1-a
    return int(a),int(b)
   
    

arr  = [1,2,3,5,6,7,8,9]
print oneMissing(arr)

arr  = [1,2,5,6,7,8,9]
print twoMissing(arr)

arr = [1,3,4,5,6,8,9]
print twoMissing(arr)


