from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Dummy node points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # 'current' pointer traverses the list
        current = dummy
        
        while current.next:
            if current.next.val == val:
                # Skip the node containing the target value
                current.next = current.next.next
            else:
                # Move to the next node only if no deletion occurred
                current = current.next
                
        return dummy.next
