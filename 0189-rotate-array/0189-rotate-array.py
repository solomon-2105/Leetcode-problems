class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=len(nums)-1
        k%=a+1
        self.reverse(nums,0,a)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,a)
        
    def reverse(self,nums,i,j):
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1