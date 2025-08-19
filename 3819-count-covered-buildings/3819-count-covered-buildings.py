import collections
import bisect

class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        col_map = collections.defaultdict(list)
        row_map = collections.defaultdict(list)
        for x, y in buildings:
            col_map[y].append(x)
            row_map[x].append(y)
        for lst in col_map.values():
            lst.sort()
        for lst in row_map.values():
            lst.sort()
        count = 0
        for x, y in buildings:
            xs = col_map[y]
            ys = row_map[x]
            xi = bisect.bisect_left(xs, x)
            yi = bisect.bisect_left(ys, y)
            has_above = xi > 0
            has_below = xi < len(xs) - 1
            has_left = yi > 0
            has_right = yi < len(ys) - 1
            if has_above and has_below and has_left and has_right:
                count += 1
        return count
