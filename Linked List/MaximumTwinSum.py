# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        Maxsum = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev,curr = None,slow
        
        while curr:
            Nextlist = curr.next
            curr.next = prev
            prev = curr
            curr = Nextlist

        first,second = head,prev
        while second:
            Maxsum = max(Maxsum,first.val + second.val)
            first = first.next
            second = second.next
        return Maxsum
