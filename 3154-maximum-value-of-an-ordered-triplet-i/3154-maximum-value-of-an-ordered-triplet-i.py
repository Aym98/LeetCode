class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        value = 0
        n = len(nums)
        max_diff = {}
        for i in range(1, n-1):
            max_diff[i] = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                max_diff[j] = max(max_diff[j], (nums[i] - nums[j]))
        for j in max_diff:
            for k in range(j+1, n):
                value = max(max_diff[j] * nums[k], value)
        return value
        