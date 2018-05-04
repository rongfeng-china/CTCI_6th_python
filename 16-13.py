def bisect_square(sq1,sq2):
    x1,x2 = sq1.cp.x,sq2.cp.x
    y1,y2 = sq2.cp.y,sq2.cp.y
    if x1 == x2:
        ys = [sq1.cp.y-sq1.length,sq1.cp.y+sq1.length,sq2.cp.y-sq2.length,sq2.cp.y+sq2.length]
        ys =sorted(ys)
        return Point(x1,ys[0]),Point(x1,ys[3])
    if y1 == y2:
        xs = [sq1.cp.x-sq1.length,sq1.cp.x+sq1.length,sq2.cp.x-sq2.length,sq2.cp.x+sq2.length]
        xs = sorted(xs)
        return Point(xs[0],y1),Point(xs[3],y1)
    tan = 1.*(y2-y1)/(x2-x1)
    if tan >= -1 and tan <= 1:
        yr1 = 1.*sq2.cp.length*(y2-y1)/(x2-x1)+y2
        yl1 = y2 - 1.*sq2.cp.length*(y2-y1)/(x2-x1)
        yr2 = 1.*sq1.cp.length*(y2-y1)/(x2-x1)+y1
        yl2 = y1 - 1.*sq1.cp.length*(y2-y1)/(x2-x1)
        Pr = Point(x2+sq2.cp.length,yr1) if ((x2+sq2.cp.length) >(x1+sq1.cp.length)) else Point(x1+sq1.cp.length,yr2)
        Pl = Point(x2-sq2.cp.length,yl1) if (x2-sq2.cp.length) < (x1-sq1.cp.length)  else Point(x1-sq1.cp.length,yl2)
        return Pl,Pr
    else:
        xt1 = 1.*sq1.cp.length*(x2-x1)/(y2-y1)+x1
        xb1 = x1-1.*sq1.cp.length*(x2-x1)/(y2-y1)
        xt2 = 1.*sq2.cp.length*(x2-x1)/(y2-y1)+x2
        xb2 = x2-1.*sq2.cp.length*(x2-x1)/(y2-y1)
        Pt = Point(xt1,y1+sq1.cp.length) if (y1+sq1.cp.length)>(y2+sq2.cp.length) else Point(xt2,y2+sq2.cp.length)
        Pb = Point(xb1,y1-sq1.cp.length) if (y1-sq1.cp.length)<(y2-sq2.cp.length) else Point(xb2,y2-sq2.cp.length)
        return Pt,Pb

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Square:
    def __init__(self,cp,length):
        self.cp = cp
        self.length = length

sq1 = Square(Point(1,2),3)
sq2 = Square(Point(4,5),6)
P1,P2 = bisect_square(sq1,sq2)
print "%.2f %.2f %.2f %.2f" %(P1.x,P1.y,P2.x,P2.y)
 
