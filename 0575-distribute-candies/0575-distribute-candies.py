class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=len(set(candyType))
        brr=len(candyType) // 2
        return min(a,brr)
        