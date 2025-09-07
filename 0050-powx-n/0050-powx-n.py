class Solution(object):
    def myPow(self, x, n):
        nn=abs(n)
        res=1
        while nn:
            if nn%2==0:
                x*=x
                nn//=2
            else:
                res*=x
                nn-=1
        if n<0:
            res=1/res
        return res

