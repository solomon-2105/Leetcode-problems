#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        const int MOD = 1e9 + 7;
        vector<vector<pair<int, int>>> adj(n);
        for (auto& road : roads) {
            int u = road[0], v = road[1], time = road[2];
            adj[u].push_back({v, time});
            adj[v].push_back({u, time});
        }
        vector<long long> dist(n, LLONG_MAX);
        vector<int> ways(n, 0);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        
        dist[0] = 0;
        ways[0] = 1;
        pq.push({0, 0});        
        while (!pq.empty()) {
            auto [time, u] = pq.top();
            pq.pop();
            if (time > dist[u]) continue;
            for (auto [v, t] : adj[u]) {
                long long newTime = time + t;
                if (newTime < dist[v]) {
                    dist[v] = newTime;
                    pq.push({newTime, v});
                    ways[v] = ways[u];  
                } 
                else if (newTime == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;  
                }
            }
        }
        
        return ways[n - 1];
    }
};
