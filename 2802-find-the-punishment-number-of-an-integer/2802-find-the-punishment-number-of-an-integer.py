class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(num,sqr):
            if sqr<num or num<0:
                return False
            if sqr==num:
                return True
            ret=False
            mul=1
            for i in range(len(str(num))):
                mul=mul*10
                ret=ret or check(num-(sqr%mul),sqr//mul)
            return ret    


        ans=0
        for i in range(1,n+1):
            if check(i,i*i):
                ans+=(i*i)
        return ans        
