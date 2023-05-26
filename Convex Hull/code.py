class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex_hull(points):

    n = len(points)

    if n < 3:
        return []

    hull = []

    l = 0
    for i in range(1, n):
        if points[i].x < points[l].x:
            l = i

    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == l:
            break

    return hull

def merge_hulls(left_hull, right_hull):
    l = len(left_hull)
    r = len(right_hull)

    if l == 0 or r == 0:
        return left_hull + right_hull

    lp = 0
    for i in range(1, l):
        if left_hull[i].x > left_hull[lp].x:
            lp = i

    rp = 0
    for i in range(1, r):
        if right_hull[i].x < right_hull[rp].x:
            rp = i

    upper_tangent = False
    lower_tangent = False
    p1 = lp
    p2 = rp

    while not (upper_tangent and lower_tangent):
        if orientation(left_hull[p1], right_hull[p2], left_hull[(p1+1)%l]) == 2:
            p1 = (p1+1)%l
        else:
            upper_tangent = True

        if orientation(right_hull[p2], left_hull[p1], right_hull[(p2-1+r)%r]) == 2:
            p2 = (p2-1+r)%r
        else:
            lower_tangent = True

    upper_chain = left_hull[:p1] + right_hull[p2:]
    lower_chain = right_hull[:p2] + left_hull[p1:]

    return convex_hull(upper_chain + lower_chain)

def convex_hull_dc(points):

    n = len(points)

    if n < 4:
        return convex_hull(points)

    mid = n // 2
    left_hull = convex_hull_dc(points[:mid])
    right_hull = convex_hull_dc(points[mid:])

    return merge_hulls(left_hull, right_hull)
