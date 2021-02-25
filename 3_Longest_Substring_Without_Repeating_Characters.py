class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        start = end = 0
        maxSize  = 0
        for index, ele in enumerate(s):
            if ele in map and map[ele]>=start:
                temp = map[ele]
                start = temp+1
                map[ele] = index
            else:
                map[ele] = index
                if end-start+1 > maxSize:
                    maxSize = end-start+1
            end+=1
        return maxSize