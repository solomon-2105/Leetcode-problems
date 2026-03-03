import math
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        #BRUTEFORCE APPROACH (SIMULATION OF RECURSION / BUILDING THE STRING FROM SCRATCH BITCHES)
        # def findit(n):
        #     if n == 1:
        #         return "0"
        #     n1 = findit(n-1)
        #     return n1 + "1" + reverse(invert(n1))
        
        # def reverse(a):
        #     return a[::-1]

        # def invert(a):
        #     res = ""
        #     for i in a:
        #         res += str(1 - int(i))
        #     return res

        # string = findit(n)
        # return string[k-1]

#===============================================================================
        
        #OPTIMAL APPROACH EASY AS FUCK

        if n == 1:
            return "0"

        length = (1 << n) - 1
        mid = (length // 2) + 1
        if k < mid:
            return self.findKthBit(n - 1, k)
        elif k == mid:
            return "1"
        else:
            ch = self.findKthBit(n - 1, length - k + 1)
            return "1" if ch == "0" else "0"