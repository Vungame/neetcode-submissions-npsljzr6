class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: 
            return True
        

        adj = {i : [] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
        
