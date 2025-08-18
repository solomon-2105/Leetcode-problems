class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        maxl,c=0,0
        for i in s:
            if i=="(":
                stack.append(i)
                c+=1
                maxl=max(maxl,c)
            elif i==")":
                stack.pop()
                c-=1
        return maxl