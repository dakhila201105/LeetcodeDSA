# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

  def hasCycle(self, head: ListNode) -> bool:
    slow = head
    fast = head

    # Move fast pointer by 2 steps and slow by 1 step
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      # If they meet, a cycle exists
      if slow == fast:
        return True

    # Fast pointer reached the end, so no cycle exists
    return False
