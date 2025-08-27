class Solution:
    def checkDivisibility(self, n: int) -> bool:

        # c=0
        # a,b=n,n
        # while a:
        #     c+=a%10
        #     a//=10
        # d=1
        # while b:
        #     d*=b%10
        #     b//=10
        # return (c+d)==n


        a,b,c=0,1,n
        while n:
            a+=n%10
            b*=n%10
            n//=10
        return c%(a+b)==0