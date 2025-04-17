class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        y = str(x)
        n = len(y)
        for i in range(int(n+1/2)):
            if y[i] != y[n-1-i]:
                return False
        return True