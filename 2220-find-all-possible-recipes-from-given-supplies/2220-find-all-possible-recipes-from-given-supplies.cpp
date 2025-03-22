class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        int n = recipes.size();
        unordered_set<string> supplySet(supplies.begin(), supplies.end());
        unordered_map<string, vector<int>> adj;
        vector<int> indegree(n, 0);
        
        for (int i = 0; i < n; i++) {
            for (const string& ing : ingredients[i]) {
                if (!supplySet.count(ing)) {
                    adj[ing].push_back(i);
                    indegree[i]++;
                }
            }
        }
        
        queue<int> q;
        vector<string> ans;
        
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        while (!q.empty()) {
            int ind = q.front();
            q.pop();
            ans.push_back(recipes[ind]);
            supplySet.insert(recipes[ind]);
            
            for (int nbr : adj[recipes[ind]]) {
                if (--indegree[nbr] == 0) {
                    q.push(nbr);
                }
            }
        }
        
        return ans;
    }
};
