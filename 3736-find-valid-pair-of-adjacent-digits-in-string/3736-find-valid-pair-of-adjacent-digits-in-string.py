class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                if s.count(s[i])==int(s[i]) and s.count(s[i+1])==int(s[i+1]):
                    return s[i]+s[i+1]
        return ""