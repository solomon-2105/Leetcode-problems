import math
class Solution:
    def minOperations(self, a: list[int]) -> int:
        g=a[0]
        for x in a[1:]:g=math.gcd(g,x)
        if g>1:return -1
        if 1 in a:return len(a)-a.count(1)
        n=len(a)
        m=n
        for i in range(n):
            g=a[i]
            for j in range(i+1,n):
                g=math.gcd(g,a[j])
                if g==1:
                    m=min(m,j-i+1)
                    break
        return m+n-2