# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
           
        node1 = node2 = head
        
        for _ in range(k-1):
            
            node1 = node1.next
        
        first_node = node1
        
        while node1.next:
            node1 = node1.next
            node2 = node2.next
            
            
            
        first_node.val, node2.val = node2.val, first_node.val
        
        return head
        
        
        
        
        
        
        