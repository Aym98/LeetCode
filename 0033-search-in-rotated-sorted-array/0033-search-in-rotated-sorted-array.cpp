class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int a = 0;
        int b = n - 1;
        while (a <= b){
            int m = (a+b) / 2;

            if (nums[m] == target) return m;
            if (nums[a] <= nums[m]) {
                if (nums[a] <= target && target < nums[m]) b = m-1;
                
                else a = m+1;
            }
            if (nums[m] <= nums[b]){
                if (nums[m] < target && target <= nums[b]) a = m+1;
                
                else b = m-1;
            }
        }
        return -1;
    }
};