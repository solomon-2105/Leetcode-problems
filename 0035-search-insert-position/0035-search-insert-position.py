class Solution:
    def searchInsert(self, a: List[int], target: int) -> int:
        ans=len(a)
        low,high=0,ans-1
        while low<=high:
            mid=low+(high-low)//2
            if a[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans