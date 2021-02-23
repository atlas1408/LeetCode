class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, ele in enumerate(nums):
            diff = target - ele
            if diff in map:
                return [map[diff], index]
            map[ele] = index