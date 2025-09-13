class Solution:
    def maxFreqSum(self, s: str) -> int:
        a={}
        b={}
        c={'a','e','i','o','u'}
        for i in s:
            if i in c:
                a[i]=a.get(i,0)+1
            else:
                b[i]=b.get(i,0)+1
        return (max(a.values()) if a else 0)+(max(b.values()) if b else 0)