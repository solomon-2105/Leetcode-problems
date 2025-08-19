class Solution {
public:
    long long coloredCells(int n) {
        long long a= n;
        return 2*(a*a) - 2*a +1;
    }
};