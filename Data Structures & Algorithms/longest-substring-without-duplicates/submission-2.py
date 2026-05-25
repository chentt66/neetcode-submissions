class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        max_length = 1
        l = 0
        r = 1
        seen = {s[l]: l}
        while r < n:
            if s[r] not in seen:
                seen[s[r]] = r
                r += 1
                max_length = max(r-l, max_length)
            else:
                l = seen[s[r]] + 1
                r = l + 1
                seen = {s[l]: l}
        return max_length