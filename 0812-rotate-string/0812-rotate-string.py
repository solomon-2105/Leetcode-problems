class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal: return True
        for i in range(1,len(s)):
            if (s[i:]+s[:i])==goal: return True
        return False