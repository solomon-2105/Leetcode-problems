class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        t = 0
        j = n
        while j:
            p = self.factorial(j%10)
            t += p
            j //= 10
        return sorted(str(n)) == sorted(str(t))
    def factorial(self , m):
        res = 1
        for i in range(1 , m+1):
            res *= i
        return res