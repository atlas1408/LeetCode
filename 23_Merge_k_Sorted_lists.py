import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        dummy = curr = ListNode(None)
        for index in range(len(lists)):
            if lists[index]:
                heap.append((lists[index].val, index, lists[index]))
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap)
            curr.next = node[2]
            curr = curr.next
            if node[2].next:
                _next = node[2].next
                heapq.heappush(heap, (_next.val, node[1], _next))
            heapq.heapify(heap)
        return dummy.next
        