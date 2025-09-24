class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        a,b=0,1
        c=2
        while c<=n:
            temp=a+b
            a=b
            b=temp
            c+=1
        return b
