class Solution {
public:
    int maxScore(string s) {
        int r_score = count(s.begin(), s.end(), '1');
        int l_score = 0;
        int max_score = 0;
        int score = 0;
        int n = s.size();
        for(int i=0; i<n-1; i++){
            if(s[i] == '0'){
                l_score ++;
            }
            if(s[i] == '1'){
                r_score --;
            }
            score = l_score + r_score;
            max_score = max(score, max_score);
        }
        return max_score;
        
    }
};