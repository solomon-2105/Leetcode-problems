class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        while True:
            if self.Binary_search(nums,original):
                original*=2
            else:
                break
        return original

    def Binary_search(self,nums,original):
        l,h=0,len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m]<original:
                l=m+1
            elif nums[m]>original:
                h=m-1
            else:
                return True
        return False