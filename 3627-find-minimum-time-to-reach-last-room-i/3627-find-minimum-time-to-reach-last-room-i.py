class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        
        n, m = len(moveTime), len(moveTime[0])
        
        # Initialize distances matrix with infinity
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0  # Start at (0,0) with time 0
        
        # Priority queue for Dijkstra's algorithm
        # Format: (arrival_time, row, col)
        pq = [(0, 0, 0)]
        
        # Four possible directions: up, right, down, left
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            time, r, c = heappop(pq)
            
            # If we've already found a better path to this cell, skip it
            if time > dist[r][c]:
                continue
                
            # If we've reached the destination, return the time
            if r == n - 1 and c == m - 1:
                return time
            
            # Try moving in all four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the new position is valid
                if 0 <= nr < n and 0 <= nc < m:
                    # We can only move TO the next room at or after moveTime[nr][nc]
                    # So we take the max of our current time and the moveTime for that room
                    earliest_possible_time = max(time, moveTime[nr][nc])
                    # Then it takes 1 second to move to that room
                    new_time = earliest_possible_time + 1
                    
                    # If this is a better path, update and add to queue
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heappush(pq, (new_time, nr, nc))
        
        return dist[n-1][m-1]