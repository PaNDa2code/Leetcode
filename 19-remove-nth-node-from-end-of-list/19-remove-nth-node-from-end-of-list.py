# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        def getLen(node):
            
            if node.next is None:
                
                return 1
            
            return 1 + getLen(node.next)
        
        
        
        r = getLen(head) - n
        
        if r == 0:
            return head.next
        

        r -= 1
        
        node = eval(f"head{'.next'*r}")
        
        
        
        node.next = node.next.next
            
            
        
        return head
        
        
        