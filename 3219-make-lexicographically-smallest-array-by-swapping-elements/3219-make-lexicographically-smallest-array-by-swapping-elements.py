class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
       groups = []
       group_mapping = {}
       for num in sorted(nums):
            if not groups or num - groups[-1][-1] > limit:
                groups.append(deque([]))
            groups[-1].append(num)
            group_mapping[num] = len(groups) - 1
      
       res = []
       for num in nums:
            group_ind = group_mapping[num]
            res.append(groups[group_ind].popleft())
       return res 