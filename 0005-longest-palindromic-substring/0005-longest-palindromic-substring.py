class Solution:
    def longestPalindrome(self, s: str) -> str:
    #     maxlen=float('-inf')
    #     sp=0
    #     n=len(s)
    #     for i in range(n):
    #         for j in range(i,n):
    #             if self.palindrome(s,i,j):
    #                 if maxlen<(j-i+1):
    #                     maxlen=j-i+1
    #                     sp=i
    #     return s[sp:sp+maxlen]
    
    # def palindrome(self,s:str,i:int,j:int)->bool:
    #     l,h=i,j
    #     while l<=h:
    #         if s[l]!=s[h]: return False
    #         else:
    #             l+=1
    #             h-=1
    #     return True
        n=len(s)
        maxlen=float('-inf')
        sp=0
        for i in range(len(s)):
            l,r=self.brr(s,i,i)
            if r-l+1>maxlen:
                maxlen=r-l+1
                sp=l
            l,r=self.brr(s,i,i+1)
            if r-l+1>maxlen:
                maxlen=r-l+1
                sp=l
        return s[sp:sp+maxlen]
    
    def brr(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return l+1,r-1