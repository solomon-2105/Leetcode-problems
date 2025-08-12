class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high=max(weights),sum(weights)
        while low<=high:
            mid=low+(high-low)//2
            res=self.Binary_search(weights,mid)
            if res<=days:
                high=mid-1
            else:
                low=mid+1
        return low
    
    def Binary_search(self,weights,mid):
        load,days=0,1
        for j in weights:
            if load+j>mid:
                load=j
                days+=1
            else:
                load+=j
        return days