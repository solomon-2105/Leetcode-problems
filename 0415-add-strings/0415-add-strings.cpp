class Solution {
public:
    string addStrings(string num1, string num2) {
        string result = "";
        int i = num1.size() - 1, j = num2.size() - 1, carry = 0;

        while (i >= 0 || j >= 0 || carry) {
            int digit1 = (i >= 0) ? (num1[i] - '0') : 0;
            int digit2 = (j >= 0) ? (num2[j] - '0') : 0;
            int sum = digit1 + digit2 + carry;
            
            result += (sum % 10) + '0';
            carry = sum / 10; 
            i--;
            j--;
        }

        reverse(result.begin(), result.end()); 
        return result;
    }
};