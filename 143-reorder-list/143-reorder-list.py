# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def preorder(head):
            result = []  # Initialize an empty list to store the linked nodes

            # Traverse the linked list and add each node to the result list
            while head is not None:
                result.append(head.val)
                head = head.next

            return result
        
        orde = preorder(head)
        
        left,right = 0 , len(orde)-1
        
        while left <= right:
            
            if left == right:
                head.val = orde[left]
            else:
                head.val, head.next.val = orde[left],orde[right]

                head = head.next.next
            
            left += 1
            
            right -= 1
            
        
        
            
            
        