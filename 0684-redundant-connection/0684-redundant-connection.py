class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        path = defaultdict(list)
        
        res = []

        def dfs(src, parent):
            if src in visited:
                return True
            visited.append(src)
            for dst in path[src]:
                if dst == parent:
                    continue
                if dfs(dst, src):
                    return True
            
            return False
        for u, v in edges:
            visited = []
            path[u].append(v)
            path[v].append(u)
            if dfs(u, -1):
                return [u, v]

        return 0

        