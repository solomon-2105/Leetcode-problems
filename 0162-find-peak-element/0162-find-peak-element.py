from typing import List
class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        c=len(a)
        low,high=0,c-1
        while low<=high:
            mid=low+(high-low)//2
            if (mid==0 and c==1) or \
   (mid==0 and a[mid]>a[mid+1]) or \
   (mid==c-1 and a[mid]>a[mid-1]) or\
   (mid>0 and mid<c-1 and a[mid]>a[mid-1] and a[mid]>a[mid+1]):
                return mid
            elif mid<c-1 and a[mid]<a[mid+1]:
                low=mid+1
            else:
                high=mid-1
