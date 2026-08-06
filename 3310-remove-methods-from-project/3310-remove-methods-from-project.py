from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for u, v in invocations:
            graph[u].append(v)
            indegree[v] += 1
        
        suspicious = set([k])
        q = deque([k])
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                indegree[v] -= 1
                if v not in suspicious:
                    suspicious.add(v)
                    q.append(v)
        
        for node in suspicious:
            if indegree[node] > 0:
                return list(range(n))  # cannot remove safely
        
        return [i for i in range(n) if i not in suspicious]
