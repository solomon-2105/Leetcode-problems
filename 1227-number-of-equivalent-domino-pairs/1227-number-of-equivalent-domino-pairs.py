class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        res = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            if key in count:
                res += count[key]
                count[key] += 1
            else:
                count[key] = 1
        return res