class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # a=b=0
        # for i in range(1,n+1):
        #     a=i
        #     b=n-i
        #     if str(a).find('0')==-1 and str(b).find('0')==-1:
        #         return [a,b]
        a,b=n,0
        pv=1
        while n>1:
            t=1
            if n%10==1: t=2
            a=a-t*pv
            b=b+t*pv
            n=(n-t)//10
            pv*=10
        return [a,b]