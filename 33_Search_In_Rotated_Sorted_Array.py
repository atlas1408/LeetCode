class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(left, right):
            if left > right:
                return -1
            mid = left + (right-left)//2
            print(mid)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                if nums[mid]<nums[right] or target>=nums[left]:
                    return bst(left, mid-1)
                else:
                    return bst(mid+1, right)
            else:
                if nums[mid]>=nums[left] or target<= nums[right]:
                    return bst(mid+1, right)
                else:
                    return bst(left, mid-1)
        return bst(0, len(nums)-1)