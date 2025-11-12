class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        presum=0
        count=0
        for i in nums:
            presum+=i

            if presum-k in a:
                count+=a[presum-k]
            
            a[presum]=a.get(presum,0)+1
        return count
            