class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums)%k !=0:
            return False
        else:
            bitch=len(nums)//k
            a={}
            for i in nums:
                a[i]=a.get(i,0)+1
            for w in a.values():
                if w>bitch: return False
            return True