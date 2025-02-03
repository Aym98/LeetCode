class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated_nums = [0] * n
        for x in range(n):
            for i in range(n):
                rotated_nums[i] = nums[(x+i)% n]
            if rotated_nums == sorted(nums):
                return True
        return False
        