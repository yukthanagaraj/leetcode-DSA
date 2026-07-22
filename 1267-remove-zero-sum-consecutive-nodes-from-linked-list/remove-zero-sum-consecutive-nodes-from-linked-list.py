class Solution:
    def removeZeroSumSublists(self, head):

        dummy = ListNode(0)
        dummy.next = head

        prefix = 0
        mp = {}

        # First pass: store last node for each prefix sum
        node = dummy
        while node:
            prefix += node.val
            mp[prefix] = node
            node = node.next

        # Second pass: remove zero-sum sublists
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            node.next = mp[prefix].next
            node = node.next

        return dummy.next