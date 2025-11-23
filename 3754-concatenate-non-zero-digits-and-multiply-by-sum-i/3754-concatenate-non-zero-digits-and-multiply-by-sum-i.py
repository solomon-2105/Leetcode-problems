class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0: return 0
        s=str(n)
        a=''
        sum=0
        for i in s:
            if i!='0':
                a+=i
                sum+=int(i)
        a=int(a)
        return sum*a