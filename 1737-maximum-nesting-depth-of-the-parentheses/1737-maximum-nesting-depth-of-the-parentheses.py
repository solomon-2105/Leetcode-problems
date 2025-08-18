class Solution:
    def maxDepth(self, s: str) -> int:
        maxl,c=0,0
        for i in s:
            if i=="(":
                c+=1
                maxl=max(maxl,c)
            elif i==")":
                c-=1
        return maxl