class Solution {
public:
    string smallestNumber(string pattern) {
        string result = "";
        stack<int> st;

        // Iterate through the pattern and push numbers accordingly
        for (int i = 0; i <= pattern.size(); i++) {
            st.push(i + 1); // Push the next number into the stack

            // When we see 'I' or reach the end, pop from the stack
            if (i == pattern.size() || pattern[i] == 'I') {
                while (!st.empty()) {
                    result += to_string(st.top());
                    st.pop();
                }
            }
        }
        
        return result;
    }
};
