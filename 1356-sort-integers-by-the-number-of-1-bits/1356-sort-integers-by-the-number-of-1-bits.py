class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(x):
            c = 0
            while x:
                c += x & 1
                x >>= 1
            return c
        
        return sorted(arr, key=lambda x: (count_bits(x), x))