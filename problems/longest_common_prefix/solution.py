class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        for i in range(1,len(strs)):
            j = 0
            while j<len(strs[i]) and j<len(strs[i-1]):
                if prefix != "" and j<len(prefix):
                    if strs[i][j] != prefix[j]:
                        break
                else:
                    if strs[i-1][j] != strs[i][j]:
                        break
                
                j += 1
            if i==1 and strs[i][:j] == strs[i-1][:j]:
                prefix = strs[i][:j]
            else:
                if strs[i][:j] == prefix[:j]:
                    prefix = strs[i][:j]
        return prefix
