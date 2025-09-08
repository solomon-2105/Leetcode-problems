class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=b=0
        for i in range(1,n+1):
            a=i
            b=n-i
            if str(a).find('0')==-1 and str(b).find('0')==-1:
                return [a,b]