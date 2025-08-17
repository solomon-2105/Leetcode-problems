class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        a={}
        for i in s:
            a[i]=a.get(i,0)+1
        for i in t:
            if i not in a or a[i]==0:
                return False
            a[i]-=1
        return True