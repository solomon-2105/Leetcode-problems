class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ass=""
        for c in s:
            if c=="(":
                if not stack:
                    stack.append(c)
                else:
                    stack.append(c)
                    ass+=c
            else:
                stack.pop()
                if stack: ass+=c
        return ass
