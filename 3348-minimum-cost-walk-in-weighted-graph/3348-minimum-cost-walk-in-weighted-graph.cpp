class DSU {
public:
    vector<int> parent, rank, minAnd;
    
    DSU(int n) : parent(n), rank(n, 0), minAnd(n, -1) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            minAnd[i] = (1 << 17) - 1;  // Max 17-bit number since 0 <= w <= 100000
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // Path compression
        }
        return parent[x];
    }

    void unite(int x, int y, int weight) {
        int rootX = find(x), rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
                minAnd[rootX] &= minAnd[rootY] & weight;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
                minAnd[rootY] &= minAnd[rootX] & weight;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
                minAnd[rootX] &= minAnd[rootY] & weight;
            }
        } else {
            minAnd[rootX] &= weight;  // Update AND value for component
        }
    }
};

class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        DSU dsu(n);
        
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            dsu.unite(u, v, w);
        }

        vector<int> result;
        for (auto& q : query) {
            int u = q[0], v = q[1];
            if (dsu.find(u) != dsu.find(v)) {
                result.push_back(-1);
            } else {
                result.push_back(dsu.minAnd[dsu.find(u)]);
            }
        }

        return result;
    }
};
