class Solution:
    def minOperations(self, q: List[List[int]]) -> int:
        res=0
        for i in range(len(q)):
            l=q[i][0]
            r=q[i][1]
            brr=self.grr(l,r)
            res+=(brr+1)//2
        return res
    
    def grr(self,l,r):
        L=1
        # R=4*L-1
        S=1
        steps=0
        while L<=r:
            R=4*L-1
            s=max(l,L)
            e=min(r,R)
            if s<=e:
                steps+=(e-s+1)*S
            S+=1
            L=L*4
        return steps