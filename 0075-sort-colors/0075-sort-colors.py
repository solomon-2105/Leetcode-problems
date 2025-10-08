class Solution:
    def sortColors(self, bitch: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid,high=0,0,len(bitch)-1
        while mid<=high:
            if bitch[mid]==0:
                bitch[mid],bitch[low]=bitch[low],bitch[mid]
                low+=1
                mid+=1
            elif bitch[mid]==1:
                mid+=1
            elif bitch[mid]==2:
                bitch[mid],bitch[high]=bitch[high],bitch[mid]
                high-=1