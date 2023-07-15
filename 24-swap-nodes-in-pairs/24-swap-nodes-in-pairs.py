# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        dummy = ListNode(0)  # Dummy node to handle the head swapping
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            
            node1 = prev.next
            
            node2 = node1.next
            
            next_pir = node2.next
            
            prev.next = node2
            
            node2.next = node1
            
            node1.next = next_pir
            
            prev = node1
            
        return dummy.next
            
            
        
        
            
            
            
            