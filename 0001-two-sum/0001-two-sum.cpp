class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap; 
        int n = nums.size();
        for (int i = 0; i < n; i++){
            int dist = target - nums[i];
            if (hashMap.count(dist)){
                return {hashMap[dist], i};
            }
            hashMap[nums[i]] = i;
        }
        return {};
    }
};