class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            distance = target - nums[i]
            if distance in hashmap : 
                return (hashmap[distance], i)
            else : 
                hashmap[nums[i]] = i
        return ()
