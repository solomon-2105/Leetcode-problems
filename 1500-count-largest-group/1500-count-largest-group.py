class Solution:
    def countLargestGroup(self, n: int) -> int:
        a={}
        for i in range(1,n+1):  
            s=0
            x=i
            while x:
                s+=x%10
                x//=10
            a[s]=a.get(s,0)+1
        max_freq=max(a.values())
        count=0
        for v in a.values():
            if v==max_freq:
                count+=1
        return count
