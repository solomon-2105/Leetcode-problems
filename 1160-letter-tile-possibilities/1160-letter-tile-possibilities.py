class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count = {}
        for c in tiles:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        return self.backtrack(count)

    def backtrack(self, count):
        total = 0
        for tile in count:
            if count[tile] > 0:
                count[tile] -= 1
                total += 1 + self.backtrack(count)
                count[tile] += 1
        return total
