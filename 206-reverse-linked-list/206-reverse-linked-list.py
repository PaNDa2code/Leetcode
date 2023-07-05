# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return 
        
        node = head
        
        arr = [node]
        
        
        
        while node.next is not None:
            
            arr.append(node.next)
            
            node = node.next if node.next is not None else None
        
        
        left = 0
        
        right = len(arr)-1
        
        while left < right:
            
            arr[left].val , arr[right].val = arr[right].val , arr[left].val
            
            left += 1
            
            right -= 1
        
        return arr[0]
        
        
        
        
        
        
        