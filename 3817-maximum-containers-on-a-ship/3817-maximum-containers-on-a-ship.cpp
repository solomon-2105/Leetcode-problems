class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        long long maxxi = 0;
        long long cells = (long long)n * n;
        long long maxContainers = maxWeight / w; 
        return min(cells, maxContainers); 
}};