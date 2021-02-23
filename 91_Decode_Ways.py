class Solution:
    def numDecodings(self, s: str) -> int:
        if s=="" or s[0] == "0":
            return 0
        map = {}
        def rec(index):
            if index > len(s)-1:
                return 1
            if s[index]=="0":
                return 0
            if index in map:
                return map[index]
            single = double = 0
            if index+1<len(s) and 1<=int(s[index:index+2])<27:
                print(s[index:index+2])
                double += rec(index+2)
            single += rec(index+1)
            map[index] = single + double
            return map[index]
        return rec(0)