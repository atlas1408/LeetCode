class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo  = {}
        def rec(index):
            if index==len(s):
                return True
            if index in memo:
                return memo[index]
            flag = False
            for ind in range(index, len(s)+1):
                if s[index:ind] in wordDict:
                    flag = rec(ind)
                    if flag:
                        memo[index] = True
                        return flag
            memo[index] = flag
            return memo[index]
        return rec(0)
        