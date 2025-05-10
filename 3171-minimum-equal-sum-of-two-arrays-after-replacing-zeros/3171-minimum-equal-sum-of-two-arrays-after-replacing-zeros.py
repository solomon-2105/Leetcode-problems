class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2=0,0
        for i in nums1:
            l1+=1
        for j in nums2:
            l2+=1
        zero1,zero2=0,0
        for i in range(l1):
            if nums1[i]==0:
                nums1[i]=1
                zero1+=1
        for i in range(l2):
            if nums2[i]==0:
                nums2[i]=1
                zero2+=1
        sum1,sum2=0,0
        for i in nums1: sum1+=i
        for j in nums2: sum2+=j 
        if (sum1<sum2 and zero1==0) or (sum1>sum2 and zero2==0): return -1
        if sum1>sum2 : return sum1
        else : return sum2