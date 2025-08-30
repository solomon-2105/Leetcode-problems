class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        i=0
        while i<len(s) and s[i]==" ": i+=1
        if i==len(s): return 0
        brr=False
        if s[i]=="-":
            brr=True
            i+=1
        elif s[i]=="+":
            i+=1
        def rec(i,num):
            if i==len(s) or not s[i].isdigit(): return num
            return rec(i+1,num*10+(ord(s[i])-ord('0')))
        num=rec(i,0)
        if brr: num*=-1
        num=max(-2**31,min(2**31-1,num))
        return num
