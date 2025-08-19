class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=[]
        brr={'1','2','3','4','5','6','7','8','9','0'}
        for i in s:
            if i in brr:
                if a:
                    a.pop()
            else:
                a.append(i)
        return "".join(a)
