class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        brr={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count=0
        for i in range(len(s)):
            if i+1<len(s) and brr[s[i]]<brr[s[i+1]]:
                count-=brr[s[i]]
            else:
                count+=brr[s[i]]
        return count