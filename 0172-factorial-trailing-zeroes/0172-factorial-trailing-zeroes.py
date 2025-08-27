class Solution:
    def trailingZeroes(self, n: int) -> int:
    #     d=self.fact(n)
    #     c=0
    #     while d%10==0:
    #         c+=1
    #         d//=10
    #     return c

    # def fact(self,n):
    #     if n==0: 
    #         return 1
    #     return n*self.fact(n-1)

        c=0
        while n:
            n//=5
            c+=n
        return c