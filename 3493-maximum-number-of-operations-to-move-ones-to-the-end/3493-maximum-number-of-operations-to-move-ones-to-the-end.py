class Solution:
    def maxOperations(self, s: str) -> int:
        brr=0
        res=0
        for i, j in enumerate(s):
            if j=='1':
                brr+=1
            elif i>0 and s[i-1]=='1':
                res+=brr
        return res