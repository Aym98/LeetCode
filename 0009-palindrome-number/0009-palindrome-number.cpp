class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0){
             return false;
              }
        int temp = x;
        long long reversed = 0;
        int remain = 0;
        while (temp != 0)
        {
            remain = temp % 10;
            reversed = reversed * 10 + remain;
            temp = temp / 10;
            
        }
        cout << reversed << endl;
        return reversed == x;
        }
};