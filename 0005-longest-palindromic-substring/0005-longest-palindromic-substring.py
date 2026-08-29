class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        for i in range(len(s)):
            # 1. Check for odd-length palindromes (centered on a single character)
            # Example: "aba" is centered on 'b'
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
                
            # 2. Check for even-length palindromes (centered between two characters)
            # Example: "abba" is centered between the two 'b's
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
                
        return res