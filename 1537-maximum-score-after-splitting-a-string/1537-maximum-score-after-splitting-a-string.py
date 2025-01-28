class Solution:
    def maxScore(self, s: str) -> int:
        r_score = s.count("1")
        l_score = 0
        score = r_score + l_score
        max_score = 0
        for i in range(len(s) -1):
            if s[i] == "0":
                l_score += 1
            if s[i] == "1":
                r_score -= 1
            score = l_score + r_score
            max_score = max(score, max_score) 
        return max_score          


        