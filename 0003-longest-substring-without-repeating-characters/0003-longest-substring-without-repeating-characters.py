class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_alphabet = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seen_alphabet:
                seen_alphabet.remove(s[left])
                left += 1

            seen_alphabet.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
            