class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set() 
        for i in range(len(s) - k + 1):
           sub = s[i:i+k]
           if sub not in seen:
               seen.add(sub)
        return len(seen) == 2**k