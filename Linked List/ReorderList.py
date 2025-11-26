# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#BRUTE FORCE APPROACH HAVING O(N) BOTH SPACE AND TIME
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head :
            return 

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        i , j = 0,len(nodes)-1
        while i < j:
            nodes[i].next = nodes[j]
            i+=1
            if i >=j :
                break
            nodes[j].next = nodes[i]
            j -=1

        nodes[i].next = None
#OPTIMAL 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #for finding the middle 
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reversing the second list

        second = slow.next
        prev =slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #merge two halfes

        first ,second = head,prev
        while second:
            temp1,temp2 = first.next ,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2




        