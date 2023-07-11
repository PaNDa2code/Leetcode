class Solution:
    def reverseKGroup(self, head, k: int):
        def reverseList(node):
            prev = None
            curr = node

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev, node

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while head:
            # Check if there are k nodes remaining
            tail = prev_group
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next  # Less than k nodes remaining

            next_group = tail.next  # Store the next group's head

            # Reverse the current group
            prev = next_group
            curr = head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Connect the reversed group to the previous group
            prev_group.next = tail
            head.next = next_group

            prev_group = head
            head = next_group

        return dummy.next
