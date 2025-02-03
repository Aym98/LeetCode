class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_incr = 0
        max_decr = 0
        incr_list = [nums[0]]
        decr_list = [nums[0]]
        start = nums[0]
        for i in range(n-1):  # Checking for increasing loop 
            if nums[i] >= nums[i+1]:
                max_incr = max(max_incr, len(incr_list))
                start = nums[i+1]
                incr_list = [start]
            else:
                incr_list.append(nums[i+1])
        start = nums[0]
        for i in range(n-1):  # Checking for decreasing loop 
            if nums[i] <= nums[i+1]:
                max_decr = max(max_decr, len(decr_list))
                start = nums[i+1]
                decr_list = [start]
            else:
                decr_list.append(nums[i+1])
        max_incr = max(max_incr, len(incr_list))
        max_decr = max(max_decr, len(decr_list))
        return max(max_incr, max_decr)
