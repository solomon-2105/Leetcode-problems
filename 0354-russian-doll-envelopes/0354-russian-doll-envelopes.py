class Solution:
    def maxEnvelopes(self, envelopes):
        # Sort envelopes first by width, and then by height in descending order
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Use dynamic programming to find the length of the longest increasing subsequence based on height
        dp = []
        for env in envelopes:
            # Perform binary search to find the position of the current envelope height
            left, right = 0, len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < env[1]:
                    left = mid + 1
                else:
                    right = mid
            # If we found a position, replace the value, otherwise append it to the result
            if left == len(dp):
                dp.append(env[1])
            else:
                dp[left] = env[1]

        return len(dp)
