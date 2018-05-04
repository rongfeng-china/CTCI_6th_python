def findDist(w1,w2,bookWords):
    l1 = bookWords[w1]
    l2 = bookWords[w2]
    n1,n2 = len(l1),len(l2)
    index1,index2,result = 0,0,[]
    while index1 < n1 and index2 < n2:
       if l1[index1] < l2[index2]:
           if index1 == n1-1:
               break
           else:
               index1 += 1
               result.append(abs(l1[index1]-l2[index2]))
       else:
           if index2 == n2-1:
               break
           else:
               index2 += 1
               result.append(abs(l2[index2]-l1[index1]))
    return min(result)

bookWords = {'table':[2,200,150,250,333,1337], 'row':[158,248,323]}
word1 = 'table'
word2 = 'row'
result = findDist(word1,word2,bookWords)
print result
