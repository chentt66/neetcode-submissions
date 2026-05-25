class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        max_length = 1 # length of the longest substring without duplicate characters.
        length = 1
        l = 0
        r = 1
        seen = {s[l]: l}
        while l < r and r < n:
            if s[r] not in seen:
                length += 1
                max_length = max(length, max_length)
                seen[s[r]] = r
                r += 1
            else:
                l = seen[s[r]] + 1
                r = l + 1
                seen = {s[l]: l}
                length = 1
        return max_length