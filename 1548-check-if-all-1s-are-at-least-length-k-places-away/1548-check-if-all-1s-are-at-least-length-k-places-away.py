class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i=0
        first,prev=0,-1-k
        # while i<len(nums):
        #     if nums[i]==1:
        #        prev=i
        #        i+=1
        #        break
        #     else:i+=1
        while i<len(nums):
            if nums[i]==1:
                first=i
                if (first-prev-1)<k:
                    return False
                prev=first
            i+=1
        return True