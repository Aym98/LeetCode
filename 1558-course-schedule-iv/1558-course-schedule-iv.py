class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        look_up = {}
        courses = [sublist[1] for sublist in prerequisites]
        def dfs(a):
            if a not in look_up:
                look_up[a] = set()
                next_nodes = [sublist[0] for sublist in 
                prerequisites if sublist[1] == a]
                look_up[a].update(next_nodes)
                for node in next_nodes:
                    look_up[a].update(dfs(node))
            return look_up[a]
        
        for a in range(numCourses):
            dfs(a)

        res = [False for x in range(len(queries))]
        
        for i in range(len(queries)):
            a = queries[i][1]
            if a not in look_up:
                continue

            b = queries[i][0]
            prereq_list = look_up[a]
            if b in prereq_list:
                res[i] = True
        return res


            

        