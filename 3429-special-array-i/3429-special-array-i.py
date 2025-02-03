import numpy as np 
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_one = nums[0:n-1]
        nums_two = nums[1:n]
        final = np.add(nums_one, nums_two)
        print(final)
        res = all(final[idx] % 2 != 0 for idx in range(0, n-1))
        return res