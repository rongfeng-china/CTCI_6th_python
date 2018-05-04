def generateParens(n,result,left_n,right_n):
    if left_n == 0:
        for i in range(len(result)):
            result[i] = result[i] + right_n *')'
        right_n = 0
        return result
    elif right_n == 0:
        return result
    elif left_n > right_n:
        print ('error')
    elif left_n == right_n:
        for i in range(len(result)):
            result[i] = result[i] + '('
            result = generateParens(n,result,left_n-1,right_n)
    else:
         result2,result3 = result.copy(),result.copy()
         for i in range(len(result)):
            result2[i] = result2[i] + '('
            result2 = generateParens(n,result2,left_n-1,right_n)
         for i in range(len(result)):
            result3[i] = result3[i] + ')'
            result3 = generateParens(n,result3,left_n, right_n-1)
         result = result2 + result3
    return result


re = generateParens(3,[''],3,3)
print re
    
