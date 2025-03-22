#include <vector>

using namespace std;

class Solution {
public:
    void dfs(int node, vector<vector<int>>& adj, vector<bool>& visited, int& size, int& edgeCount) {
        visited[node] = true;
        size++;
        edgeCount += adj[node].size();
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited, size, edgeCount);
            }
        }
    }
    
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        vector<bool> visited(n, false);
        
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int size = 0, edgeCount = 0;
                dfs(i, adj, visited, size, edgeCount);
                
                if (edgeCount / 2 == size * (size - 1) / 2) {
                    count++;
                }
            }
        }
        
        return count;
    }
};
