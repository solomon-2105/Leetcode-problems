#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        int n = right;
        vector<int> primes = sieve(n), p;
        
        for (int i = left; i <= right; i++) {
            if (primes[i]) p.push_back(i);
        }

        if (p.size() < 2) return {-1, -1};

        int d = INT_MAX, a = -1, b = -1;
        for (int i = 1; i < p.size(); i++) {
            if (p[i] - p[i - 1] < d) {
                d = p[i] - p[i - 1];
                a = p[i - 1], b = p[i];
            }
        }
        return {a, b};
    }

private:
    vector<int> sieve(int n) {
        vector<int> s(n + 1, 1);
        s[0] = s[1] = 0;
        for (int i = 2; i * i <= n; i++) {
            if (s[i]) {
                for (int j = i * i; j <= n; j += i) {
                    s[j] = 0;
                }
            }
        }
        return s;
    }
};
