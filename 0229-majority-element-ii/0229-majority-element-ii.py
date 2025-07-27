import math
class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        c1,c2,el1,el2,n=0,0,None,None,len(a)
        for i in a:
            if c1==0 and i!=el2:
                c1=1
                el1=i
            elif c2==0 and i!=el1:
                c2=1
                el2=i
            elif i==el1:
                c1+=1
            elif i==el2:
                c2+=1
            else:
                c1-=1
                c2-=1
        brr,grr=0,0
        for i in a:
            if i==el1:brr+=1
            elif i==el2:grr+=1
        suiii=[]
        if brr>math.floor(n/3):
            suiii.append(el1)   
        if grr>math.floor(n/3):
            suiii.append(el2)
        return suiii
        