#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<unordered_set<int>> adj(n);
        vector<bool> visited(n, false);
        
        for (auto& edge : edges) {
            adj[edge[0]].insert(edge[1]);
            adj[edge[1]].insert(edge[0]);
        }
        
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                queue<int> q;
                unordered_set<int> component;
                q.push(i);
                visited[i] = true;
                
                while (!q.empty()) {
                    int node = q.front();
                    q.pop();
                    component.insert(node);
                    
                    for (int neighbor : adj[node]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            q.push(neighbor);
                        }
                    }
                }
                
                int size = component.size();
                int edgeCount = 0;
                
                for (int node : component) {
                    edgeCount += adj[node].size();
                }
                
                if (edgeCount / 2 == size * (size - 1) / 2) {
                    count++;
                }
            }
        }
        
        return count;
    }
};
