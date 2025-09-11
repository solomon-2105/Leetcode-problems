class Solution:
    def sortVowels(self, s: str) -> str:
        a=[]
        se={'a','e','i','o','u'}
        for i in s:
            if i.lower() in se:
                a.append(i)
        a.sort()
        res=""
        for i in s:
            if i.lower() in se:
                res+=a[0]
                a.pop(0)
            else:
                res+=i
        return res