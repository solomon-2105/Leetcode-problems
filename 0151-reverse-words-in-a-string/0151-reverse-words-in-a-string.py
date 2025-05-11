class Solution:
    def reverseWords(self, s):
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        s = list(s)
        n = len(s)

        # Step 1: Reverse the entire string
        reverse(s, 0, n - 1)

        i = 0  # read pointer
        j = 0  # write pointer

        while i < n:
            # Skip spaces
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break

            # Write a space if not the first word
            if j > 0:
                s[j] = ' '
                j += 1

            start = j

            # Copy the word
            while i < n and s[i] != ' ':
                s[j] = s[i]
                j += 1
                i += 1

            # Reverse the word in-place
            reverse(s, start, j - 1)

        # Resize the string to remove trailing content
        return ''.join(s[:j])
