class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ass=[]
        count=0
        for c in s:
            if c=="(":
                if count>0: ass.append(c)
                count+=1
            else:
                count-=1
                if count>0: ass.append(c)
        return "".join(ass)