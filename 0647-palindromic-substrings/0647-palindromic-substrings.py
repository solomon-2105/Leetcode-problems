class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.ispal(s[i:j+1]):
                    c+=1
        return c

    def ispal(self,s):
        return s==s[::-1]