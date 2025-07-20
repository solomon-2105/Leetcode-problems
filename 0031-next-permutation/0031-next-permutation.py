class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        crr=-1
        for i in range(len(a)-1,0,-1):
            if a[i-1]<a[i]:
                crr=i-1
                break
        if crr==-1:
            a.reverse()
            return
        for i in range(len(a)-1,0,-1):
            if a[i]>a[crr]:
                a[i],a[crr]=a[crr],a[i]
                break
        low=crr+1
        high=len(a)-1
        while low<high:
            a[low],a[high]=a[high],a[low]
            low+=1
            high-=1