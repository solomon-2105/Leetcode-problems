class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a,b={},{}
        for i in range(len(s)):
            if (s[i] in a and a[s[i]]!=t[i]) or (t[i] in b and b[t[i]]!=s[i]):return False
            a[s[i]]=t[i]
            b[t[i]]=s[i]
        return True