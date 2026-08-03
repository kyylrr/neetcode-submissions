class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        string = set()
        res = 0
        for right in range(len(s)):
            while s[right] in string:
                string.remove(s[left])
                left+=1
            string.add(s[right])
            res = max(res, right - left +1)
        return res
        