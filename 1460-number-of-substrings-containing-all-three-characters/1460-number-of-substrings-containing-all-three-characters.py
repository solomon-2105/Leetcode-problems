class Solution(object):
    def numberOfSubstrings(self, s):
        count = [0, 0, 0]
        left = 0
        result = 0
        n = len(s)

        for right in range(n):
            count[ord(s[right]) - ord('a')] += 1
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
            result += left

        return result