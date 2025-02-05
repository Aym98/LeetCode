class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        incr_list = [nums[0]]
        start = nums[0]
        for i in range(n-1):  # Checking for increasing loop 
            if nums[i] >= nums[i+1]:
                max_sum = max(max_sum, sum(incr_list))
                start = nums[i+1]
                incr_list = [start]
            else:
                incr_list.append(nums[i+1])
        max_sum = max(max_sum, sum(incr_list))
        return max_sum