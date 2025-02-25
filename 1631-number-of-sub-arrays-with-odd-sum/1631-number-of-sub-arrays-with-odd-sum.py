class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        current_sum = 0
        even_sum = 0
        odd_sum = 0
        res = 0
        MOD = (10 ** 9) + 7
        for n in arr:
            current_sum += n
            if current_sum % 2 == 0:
                res = (res + odd_sum) % MOD
                even_sum += 1
            else : 
                res = (res + 1 + even_sum) % MOD
                odd_sum += 1
        return res 