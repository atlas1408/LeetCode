class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        startI = intervals[0][0]
        endI = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] <= endI:
                endI = max(endI, interval[1])
            else:
                result.append([startI, endI])
                startI = interval[0]
                endI = interval[1]
        result.append([startI, endI])
        return result