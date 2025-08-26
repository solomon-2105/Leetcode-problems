class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = [0] * 1001
        for n in nums1:
            count[n]+=1
        ans=[]
        for n in nums2:
            if count[n]>0:
                ans.append(n)
                count[n]-=1
        return ans