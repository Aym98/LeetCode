class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        for a, b in edges:    #Get the dajency mapping
            adj[a].append(b)
            adj[b].append(a)
        def bfs(a):
            q = deque([(a, 1)])
            groups = {a : 1}
            while q:
                node, groupe = q.popleft()
                for nei in adj[node]:
                    if nei in groups:
                        if groups[nei] == groupe:
                            return None, -1
                        continue
                    q.append((nei, groupe+1))
                    groups[nei] = groupe + 1
                    visited.add(nei)
            return groups, max(groups.values())
        max_group = 0 
        for i in range(1, n+1):
            group_i = 0
            if i in visited:
                continue
            visited.add(i)
            groups, num_groups = bfs(i)
            if num_groups == -1:
                return -1
            for src in groups:
                _, length = bfs(src)
                group_i = max(group_i, length)
            max_group += group_i
        return max_group
        