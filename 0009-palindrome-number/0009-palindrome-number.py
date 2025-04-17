class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        y = str(x)
        n = len(y)
        j = n-1
        i = 0
        while i < j:
            if y[i] != y[j]:
                return False
            i += 1
            j -= 1
        return True