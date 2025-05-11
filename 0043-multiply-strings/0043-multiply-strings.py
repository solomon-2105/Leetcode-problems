class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)
        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                mul = digit1 * digit2

                sum_ = mul + result[i + j + 1]
                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10

        ans = ""
        for num in result:
            if not (ans == "" and num == 0):
                ans += chr(num + ord('0'))

        return ans
