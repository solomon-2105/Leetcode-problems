class Solution(object):
    def largestTriangleArea(self, points):
        max_area2 = 0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area2 = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
                    if area2 > max_area2:
                        max_area2 = area2
        return max_area2 / 2.0