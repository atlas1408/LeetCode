class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s: return False
        deleted = False
        def rec(start, end):
            nonlocal deleted
            if start>=end:
                return True
            if s[start] == s[end]:
                while start<end and s[start] == s[end]:
                    start+=1
                    end-=1
                return rec(start, end)
            else:
                if deleted: return False
                deleted = True
                return rec(start, end-1) or rec(start+1, end)
        return rec(0, len(s)-1)