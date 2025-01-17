def samePoint(p1, p2) :
    return (p1.x == p2.x) and (p1.y == p2.y)
p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4
samePoint(p1, p2)