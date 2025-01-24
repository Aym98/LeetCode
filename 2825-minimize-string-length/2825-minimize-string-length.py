class Solution:
    def minimizedStringLength(self, s: str) -> int:
        res = 0
        for cnt in Counter(s):
            res += 1
        return res