# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        out = ListNode()
        node = out
        
        while list1 is not None and list2 is not None:
            
            if list1.val <= list2.val:
                node.val = list1.val
                # node.next = ListNode()
                list1 = list1.next
                
            else:
                node.val = list2.val
                # node.next = ListNode()
                
                list2 = list2.next 
             
            
            if list1 is not None and list2 is not None:
                node.next = ListNode()
                node = node.next
        
        if list1 is not None:
            node.next = list1
        if list2 is not None:
            node.next = list2
            
        return out
    
        