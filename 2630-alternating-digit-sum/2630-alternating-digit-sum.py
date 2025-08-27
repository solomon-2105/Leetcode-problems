import math
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        c=True
        sum=0
        d=int(math.log10(n))+1
        if d%2==1:
            while n:
                if c:
                    c=False
                    sum+= (1*(n%10))
                    n//=10
                else:
                    c=True
                    sum+= (-1*(n%10))
                    n//=10
        else:
            while n:
                if c:
                    c=False
                    sum+= (-1*(n%10))
                    n//=10
                else:
                    c=True
                    sum+= (1*(n%10))
                    n//=10
        return sum