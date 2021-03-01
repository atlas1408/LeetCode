class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(", "]":"[","}":"{"}
        stack = []
        for each in s:
            if each not in map:
                stack.append(each)
            else:
                if stack and stack[-1] == map[each]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False