class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        # n=len(nums)
        # res=0
        # for i in range(n):
        #     xor=0
        #     even=odd=0
        #     for j in range(i,n):
        #         xor^=nums[j]
        #         if nums[j]%2==0:
        #             even+=1
        #         else:
        #             odd+=1
        #         if xor==0 and even==odd:
        #             res=max(res,j-i+1)
        # return res
        brr={(0,0):-1}
        result=0
        x=b=0
        for i in range(len(nums)):
            x^=nums[i]
            if nums[i]%2==0:
                b+=1
            else:
                b-=1
            grr=(x,b)
            if grr in brr:
                result=max(result,i-brr[grr])
            else:
                brr[grr]=i
        return result