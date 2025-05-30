class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True
        a=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                a.append(i)
            if len(a)>2:
                return False
        if len(a)!=2:
            return False
        i,j=a
        return s1[i]==s2[j] and s1[j]==s2[i]