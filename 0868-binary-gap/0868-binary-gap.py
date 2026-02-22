class Solution:
    def binaryGap(self, n: int) -> int:
        maxi = float('-inf')
        c = 1
        a = ""
        while n:
            a += str(n%2)
            n //= 2
        s = "".join(reversed(a))
        found = False
        for i in s:
            if i == '1':
                if found:
                    maxi = max(c , maxi)
                found = True
                c = 1
            else:
                if found:
                    c += 1
        return maxi if maxi != float('-inf') else 0