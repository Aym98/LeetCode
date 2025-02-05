class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False 
        if s1 == s2:
            return True
        n = len(s1)
        for i in range(n):
            for j in range(n):
                temp = list(s1) 
                a, b = temp[i], temp[j]
                temp[i], temp[j] = b, a

                if temp == list(s2):
                    return True
        return False 