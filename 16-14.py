def best_line(points):
    n = len(points)
    dict = {} ## dict[k,b] = 0
    for i in range(n):
        p1 = points[i]
        for j in range(n):
            if i != j:
                p2 = points[j]
                if p1.x == p2.x:                  ##### x = c
                    if p1.x in dict:
                        dict[None,p1.x] += 1
                    else:
                        dict[None,p1.x] = 1
                else:
                    k = 1.0*(p2.y-p1.y)/(p2.x-p1.x) ######### y = kx + b
                    b = p1.y - k* p1.x
                    k_round = round(k,3)
                    b_round = round(b,3)
                    if (k_round,b_round) in dict:
                        dict[k_round,b_round] += 1
                    else:
                        dict[k_round,b_round] = 1
    dict2 = list(sorted(dict.iteritems(),key=lambda x:x[1]))
    print dict2[-1][1]
    if dict2[-1][0][0] != None:
        print 'Equation is y = %.3f x + %.3f' %(dict2[-1][0][0],dict2[-1][0][1])
    else:
        print 'Equation is x = %.3f' %(dict2[-1][0][1]) 
                        

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4) ,Point(5,8)]
best_line(points)
