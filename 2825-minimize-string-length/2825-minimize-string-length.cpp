class Solution {
public:
    int minimizedStringLength(string s) {
      std::map<char, int> count;
      for(int i=0; i < s.size(); i++){
        count[s[i]]++;
      }
      
    
      return count.size();

        
    }
};