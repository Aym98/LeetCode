class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False 
        if s1 == s2:
            return True
        s1 = list(s1)
        s2 = list(s2)
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]