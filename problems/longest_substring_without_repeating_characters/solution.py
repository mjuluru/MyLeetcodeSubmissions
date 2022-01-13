class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        result = 0
        for i in range(0,len(s)):
            sub = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in sub:
                    sub = sub + s[j]
                else:
                    break
            if result < len(sub):
                result = len(sub)
        return result