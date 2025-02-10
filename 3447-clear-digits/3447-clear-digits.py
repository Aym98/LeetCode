class Solution:
    def clearDigits(self, s: str) -> str:
        if s == "":
            return s
        else:
            if not bool(re.search(r'\d', s)):
                return s 
            else : 
                for i in range(len(s)):
                    if s[i].isdigit():
                        if i == 0:
                            s1 = s[i+1 : ]
                        if i == len(s) - 1:
                            s1 = s[: i-1]
                        else : 
                            s1 = s[: i-1] + s[i+1 : ]
                        return self.clearDigits(s = s1)
