class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l=[]
        n=len(s)
        for i in range(0,n,k):
            brr=s[i:i+k]
            if len(brr)<k:
                brr+=fill*(k-len(brr))  
            l.append(brr)
        return l