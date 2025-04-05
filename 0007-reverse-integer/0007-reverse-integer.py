class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        summ=0
        while(x!=0):
            summ=summ*10+x%10
            x//=10
        if summ<-2**31 or summ>2**31-1: return 0
        return sign*summ