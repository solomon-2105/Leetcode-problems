class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_sum = 0
        min_val = 0
        max_val = 0
        for diff in differences:
            prefix_sum += diff
            min_val = min(min_val, prefix_sum)
            max_val = max(max_val, prefix_sum)
        return max(0, (upper - max_val) - (lower - min_val) + 1)
