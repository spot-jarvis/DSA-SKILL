class Solution {
public:
    bool isPalindrome(string s) {
       string cleaned;
       for(char c : s)
       if(isalnum(c))
        cleaned += tolower(c);
        return checkpalindrome(cleaned,0);
    }
private:
    bool checkpalindrome(const string &s , int i)
    {   
        int n = s.size();
        if(i >= n/2) return true;
        if(s[i] != s[n-i-1]) return false;
        return checkpalindrome(s,i+1);
    }
};
