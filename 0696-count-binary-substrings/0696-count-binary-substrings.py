class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur , prev = 1 , 0
        res = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1] : cur += 1
            else : 
                res += min(cur , prev)
                prev = cur
                cur = 1
        res += min(cur , prev)
        return res