# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        
        # Function to find kth node
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            kth = getKth(groupPrev, k)

            # Less than k nodes left
            if not kth:
                break

            groupNext = kth.next

            # Reverse group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect reversed group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next
        