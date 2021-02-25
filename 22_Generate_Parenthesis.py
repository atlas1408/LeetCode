class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result  = set()
        def rec(Open, Close, seen):
            nonlocal result
            if Open == Close and 2*Open == 2*n:
                result.add("".join(seen[:]))
                return
            if Open> n or Close > n:
                return
            if Close>Open:
                return
            rec(Open+1, Close, seen + ["("])
            rec(Open, Close+1, seen + [")"])
            return 
        rec(0, 0, [])
        return result