class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findit(n):
            if n == 1:
                return "0"
            n1 = findit(n-1)
            return n1 + "1" + reverse(invert(n1))
        
        def reverse(a):
            return a[::-1]

        def invert(a):
            res = ""
            for i in a:
                res += str(1 - int(i))
            return res

        string = findit(n)
        return string[k-1]