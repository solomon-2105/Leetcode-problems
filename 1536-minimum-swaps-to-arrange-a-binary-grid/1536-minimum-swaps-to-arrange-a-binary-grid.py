class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        endZeroes = []
        n = len(grid)
        for i in range(n):
            c = 0
            j = n - 1
            while j>=0 and grid[i][j] == 0:
                c += 1
                j -= 1
            endZeroes.append(c)
        steps = 0
        for i in range(n):
            need = n - i - 1
            j = i
            while j < n and endZeroes[j] < need:
                j += 1
            if j == n:
                return -1
            steps += j - i
            while j > i:
                endZeroes[j] , endZeroes[j-1] = endZeroes[j-1] , endZeroes[j]
                j -= 1
        return steps