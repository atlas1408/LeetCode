import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        heap = heapq.heapify(temp)
        while nums:
            heapq.heappush(temp, nums.pop())
            if len(temp)>k:
                heapq.heappop(temp)
            heapq.heapify(temp)
        return heapq.heappop(temp)