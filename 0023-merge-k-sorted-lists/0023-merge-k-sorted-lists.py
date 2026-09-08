# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        # Min-heap stores elements as tuples: (node_value, unique_counter, node_object)
        min_heap = []
        counter = 0
        
        # Initialize the heap with the head of each non-empty linked list
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, counter, head))
                counter += 1
                
        # Process the heap until it's empty
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            
            # Append the smallest node to our merged list
            current.next = node
            current = current.next
            
            # If the popped node has a next node, push it onto the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
                
        return dummy.next