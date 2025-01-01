class Solution {
public:
    int mySqrt(int x) { 
        
        int a = 0;
        int b = x;
        if (x==0 || x==1){
            return x;
        }
        while (a <= b){
            int m = (a+b)/2;
            if (pow(m, 2) == x || (pow(m, 2) <x &&pow(m+1, 2) > x))
                return m;
            
            else if (pow(m, 2) < x)
                a = m + 1;
            
            else if (pow(m, 2))
                b = m - 1;
            
        }
        return 0;
    }
};