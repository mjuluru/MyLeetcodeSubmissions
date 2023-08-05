class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        bottomUpDp = [False]*(len(s)+1)
        bottomUpDp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if ( bottomUpDp[j] and s[j:i] in wordDictSet):
                    bottomUpDp[i] = True
                    break
        return bottomUpDp[-1]

