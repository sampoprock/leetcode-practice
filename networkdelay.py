# There are N network nodes, labelled 1 to N.

# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

# Example 1:



# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        nodeDict = collections.defaultdict(list)
        inNodes  = collections.Counter()
        for u, v, w in times:
            nodeDict[u].append([v, w])
            inNodes[v] += 1
        print (inNodes)
        
        tTable = [float('inf') for _ in range(N)]
        
        visited = set()
        queue = collections.deque()
        
        queue.append([K, 0])
        tTable[K - 1] = 0
        visited.add(K)
        maxw = float('-inf')
        
        while queue:
            nc, wc = queue.popleft()
            for nt, wt in nodeDict[nc]:
                visited.add(nt)
                if tTable[nt - 1] > wc + wt:
                    tTable[nt - 1] = wc + wt
                    queue.append([nt, tTable[nt - 1]])

        if len(visited) == N:
            return max(tTable)
        else:
            return -1
        