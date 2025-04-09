class Solution:
    def frequencySort(self, s: str) -> str:
        a={}
        for i in s:
            if i in a: a[i]+=1
            else: a[i]=1
        res=""
        while a:
            max_char=max(a,key=a.get)
            res+=max_char * a[max_char]
            del a[max_char]
        return res