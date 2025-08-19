class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n=len(s)
        for i in range(n-k+1):
            if s[i:i+k]==s[i]*k:
                if (i==0 or s[i-1]!=s[i]) and (i+k==n or s[i+k]!=s[i]):
                    return True
        return False