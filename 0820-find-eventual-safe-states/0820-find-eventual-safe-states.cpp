
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        std::map<int, bool> is_safe;
        std::vector<int> safe_nodes; 
        int n = graph.size();
        std::function<bool(int)> check_safety = [&is_safe, graph, &check_safety](int i) -> bool {
            bool res = false;
            if (is_safe.count(i) > 0){
            res = is_safe[i];
            return res;
            }
            is_safe[i] = false;
            for(int nei : graph[i]){
                if (!check_safety(nei)){
                    res = false;
                return res; 
                }
            }
            is_safe[i] = true;
            res = true;
            return res;
        };
        for(int i=0; i<n; i++){
            if (check_safety(i)) {safe_nodes.insert(safe_nodes.end(), i);}
        }
        return safe_nodes;
    }
};