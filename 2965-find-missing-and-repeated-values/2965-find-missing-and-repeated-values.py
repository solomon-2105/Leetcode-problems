class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s , q = 0 , 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                s += grid[i][j]
                q += grid[i][j] ** 2
        sn , qn = 0 , 0
        for i in range(1, (n**2) +1):
            sn += i
            qn += i ** 2
        diff = s - sn
        summation = (q - qn) // diff
        m = (summation + diff) // 2
        r = summation - m
        return [m,r]