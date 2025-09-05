class Solution:
    def numberOfPairs(self, p: List[List[int]]) -> int:
        count=0
        for i in range(len(p)):
            c,d=p[i]
            for j in range(len(p)):
                if j!=i:
                    a,b=p[j]
                    if c<=a and d>=b:
                        brr=True
                        for k in range(len(p)):
                            if k!=i and k!=j:
                                q,r=p[k]
                                if c<=q<=a and b<=r<=d:
                                    brr=False
                        if brr:count+=1
        return count
