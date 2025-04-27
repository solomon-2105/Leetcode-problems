class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=i=0
        brr=dict()
        for j in range(len(s)):
            if s[j] in brr and brr[s[j]]>=i:
                i=brr[s[j]]+1
            brr[s[j]]=j
            maxi=max(maxi,j-i+1)
        return maxi 