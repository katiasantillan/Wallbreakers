class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(not s):
            return True
        
        s = s.lower()
        
        s = [i for i in s if i.isalnum()]

        return(s[::] == s[::-1])