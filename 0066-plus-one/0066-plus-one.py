class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        carry = 0
        n = len(digits)
        for i in range(n - 1 , -1 , -1) :
            
            if i == n - 1 :
                count = digits[i] + 1
            else : 
                count = digits[i] + carry
                
            if count > 9 : 
                digits[i] = count % 10
                carry = count // 10
                if i == 0:
                    digits.insert(0 , carry)
                    break
            else :
                digits[i] = count % 10
                break
        return digits