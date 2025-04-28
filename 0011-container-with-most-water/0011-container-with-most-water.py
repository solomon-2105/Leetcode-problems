class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxii=0
        i,j=0,len(height)-1
        while i<j:
            wid= j-i
            area=min(height[j],height[i])*wid
            maxii=max(maxii,area)
            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        return maxii