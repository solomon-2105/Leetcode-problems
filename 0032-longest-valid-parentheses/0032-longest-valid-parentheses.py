class Solution:
    def longestValidParentheses(self, s):
        stack = []
        stack.append(-1)
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curr_len = i - stack[-1]
                    if curr_len > max_len:
                        max_len = curr_len

        return max_len
