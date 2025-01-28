class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        def score_left(s):
            score = 0
            for i in range(len(s)):
                if s[i] == "0":
                    score += 1
            return score
        def score_right(s):
            score = 0
            for i in range(len(s)):
                if s[i] == "1":
                    score += 1
            return score
        for i in range(1, len(s)):
            sub_l = s[:i]
            sub_r = s[i : ]
            max_score = max(max_score, score_left(sub_l) + score_right(sub_r))
        return max_score



        