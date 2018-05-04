def intersection(seg1,seg2):
    if (seg1.p1.x - seg1.p2.x)*(seg2.p1.y - seg2.p2.y) == (seg2.p1.x - seg2.p2.x)*(seg1.p1.y - seg1.p2.y):
        return 'Parallel or the same line','Parallel or the same line'
    v1 = (seg1.p1.y - seg1.p2.y)*(seg2.p1.y-seg2.p2.y)*(seg1.p1.x-seg2.p1.x) + (seg2.p1.x-seg2.p2.x)*(seg1.p1.y-seg1.p2.y)*seg2.p1.y-(seg1.p1.x-seg1.p2.x)*(seg2.p1.y - seg2.p2.y)*seg1.p1.y

    v2 = (seg2.p1.x - seg2.p2.x)*(seg1.p1.y - seg1.p2.y)-(seg1.p1.x - seg1.p2.x)*(seg2.p1.y - seg2.p2.y)
    b = 1.*v1/v2
    a = seg1.p1.x - 1.*(seg1.p1.x-seg1.p2.x)/(seg1.p1.y - seg1.p2.y)*(seg1.p1.y - b)
    return a,b

class Segment:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

seg1 = Segment(Point(1,1), Point(4,4))
seg2 = Segment(Point(3,3), Point(7,7))
a,b = intersection(seg1,seg2)
print '%s, %s' %(str(a),str(b))

seg1 = Segment(Point(1,1), Point(4,4))
seg2 = Segment(Point(5,5), Point(8,8))
a,b = intersection(seg1,seg2)
print '%s, %s' %(str(a),str(b))


seg1 = Segment(Point(1,1), Point(4,4))
seg2 = Segment(Point(3,-3), Point(-2,2))
a,b = intersection(seg1,seg2)
print '%s, %s' %(str(a),str(b))

seg1 = Segment(Point(-1,-1), Point(4,4))
seg2 = Segment(Point(3,-3), Point(-2,2))
a,b = intersection(seg1,seg2)
print '%s, %s' %(str(a),str(b))

seg1 = Segment(Point(0,-1), Point(5,4))
seg2 = Segment(Point(4,-3), Point(-1,2))
a,b = intersection(seg1,seg2)
print '%s, %s' %(str(a),str(b))

seg1 = Segment(Point(0,1), Point(5,6))
seg2 = Segment(Point(4,-1), Point(-1,4))
a,b = intersection(seg1,seg2)
print '%s, %s' %(str(a),str(b))

seg1 = Segment(Point(0,1), Point(10,31))
seg2 = Segment(Point(0,4.5), Point(10,28.5))
a,b = intersection(seg1,seg2)
print '%s, %s' %(str(a),str(b))

