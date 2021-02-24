class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]*len(nums)
        prev = 1
        for index, ele in enumerate(nums):
            product[index] = prev
            prev = prev * ele
        prev = 1
        for index in range(len(nums)-1, -1, -1):
            temp = nums[index]
            nums[index] = prev
            prev = prev * temp
        for index, ele in enumerate(product):
            product[index] *= nums[index]
        return product