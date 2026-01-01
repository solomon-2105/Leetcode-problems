class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n - 1 , -1 , -1) :
            carry += digits[i] 
            if carry > 9 : 
                digits[i] = carry % 10
                carry = 1
            else :
                digits[i] = carry
                carry=0
                break
        if carry == 1 :
            digits.insert(0 , carry)
        return digits