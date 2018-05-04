def sparseSim(files):
    dict1 = {}
    for index in range(len(files)):
        for item in files[index]:
            if item in dict1:
                tmp_list = dict1[item]
                tmp_list.append(index)
                dict1[item] = tmp_list
            else:
                dict1[item] = [index]
    dict2 = {}
    for word in dict1:
        docList = dict1[word]
        n = len(docList)
        if n < 2:
            continue
        else:
            for i in range(n-1):
                for j in range(i+1,n):
                    u,v = docList[i],docList[j]
                    if (u,v) in dict2:
                        tmp_list = dict2[u,v]
                        tmp_list.append(word)
                        dict2[u,v] = tmp_list
                    else:
                        dict2[u,v] = [word]
    
    for key in dict2:
        m,n = key
        similar = len(dict2[key])
        total = len(files[m])+len(files[n])
        tmp_result = 1.0*similar/(total-similar)
        print '%d %d : %f' %(m,n,tmp_result)

    

                 
f1 = {14, 15, 100, 9, 3}
f2 = {32, 1, 9, 3, 5}
f3 = {15, 29, 2, 6, 8, 7}
f4 = {10, 7}
f5 = {1, 5, 3}
f6 = {1, 7, 2, 3}
files = [f1, f2, f3, f4, f5, f6]
sparseSim(files)
