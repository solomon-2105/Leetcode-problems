class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        a = {}
        res = ""
        for i in range(len(weights)):
            a[chr(i+97)] = weights[i]
        b = {}
        for word in words:
            score = 0
            for i in word:
                score += a[i]
            score %= 26
            res += chr(122-score)
        return res