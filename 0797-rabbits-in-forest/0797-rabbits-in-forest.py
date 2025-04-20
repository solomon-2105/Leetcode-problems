import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        a=dict()
        for i in answers:
            if i in a: a[i]+=1
            else: a[i]=1
        brr=0
        for k,v in a.items():
            s=k+1
            g=math.ceil(v/s)
            brr+=s*g
        return brr