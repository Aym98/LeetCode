class Solution:  
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        status = {}
        safe_nodes = []
        def is_safe(i):
            if i in status:
                return status[i]
            else:
                status[i] = False
                for nei in graph[i]:
                    if  not is_safe(nei):
                        return status[i]
                status[i] = True
                return status[i]
        for i in range(len(graph)):
            if is_safe(i):
                safe_nodes.append(i)
        return safe_nodes
            
        