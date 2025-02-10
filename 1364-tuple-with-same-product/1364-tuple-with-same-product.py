class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        lookUp = {}
        nums = sorted(nums)
        n = len(nums) 
        for i in range(n):
            for j in range(i+1, n):
                lookUp[(nums[i], nums[j])] = nums[i] * nums[j] 
        freq = defaultdict(int)
        res = 0
        for key, val in lookUp.items():
            freq[val] += 1
        for val in freq:
            if freq[val] > 1:
                res += 8 * math.comb(freq[val], 2)
        return res