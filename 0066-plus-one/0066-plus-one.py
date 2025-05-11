class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits are 9, we need to add a 1 at the beginning
        digits.insert(0, 1)
        return digits
