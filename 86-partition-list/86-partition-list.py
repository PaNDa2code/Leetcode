# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # [1,4,3,2,5,2]    
        s_head = s_tail = ListNode(0)
        g_head = g_tail = ListNode(0)
        
        node = head
        
        while node:
            
            if node.val < x:
                s_tail.next = node
                s_tail = s_tail.next
            else:
                g_tail.next = node
                g_tail = g_tail.next
                
            node = node.next
            
        s_tail.next = g_head.next
        g_tail.next = None
            
        
        return s_head.next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head

#         smaller_head = smaller_tail = ListNode(0)
#         greater_head = greater_tail = ListNode(0)

#         node = head
#         while node:
#             if node.val < x:
#                 smaller_tail.next = node
#                 smaller_tail = smaller_tail.next
#             else:
#                 greater_tail.next = node
#                 greater_tail = greater_tail.next
#             node = node.next

#         smaller_tail.next = greater_head.next
#         greater_tail.next = None

#         return smaller_head.next
