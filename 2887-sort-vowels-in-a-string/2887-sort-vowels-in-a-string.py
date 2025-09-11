class Solution:
    def sortVowels(self, s: str) -> str:
        a=[]
        se={'a','e','i','o','u'}
        for i in s:
            if i.lower() in se:
                a.append(i)
        a.sort()
        res=""
        j=0
        for i in s:
            if i.lower() in se:
                res+=a[j]
                j+=1
            else:
                res+=i
        return res