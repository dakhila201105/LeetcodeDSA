from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # Temporarily store the next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr       # Move the 'prev' pointer one step forward
            curr = nxt        # Move the 'curr' pointer one step forward
            
        return prev  # 'prev' ends up as the new head of the reversed list
