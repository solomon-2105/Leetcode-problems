class Solution:
    def generate(self, n: int) -> List[List[int]]:
        grr=[]
        for i in range(n):
            res=1
            brr=[1]
            for j in range(1,i+1):
                res*=(i-j+1)
                res//=j
                brr.append(res)
            grr.append(brr)
        return grr