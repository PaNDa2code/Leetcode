# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        def list_len(head):
            
            if head.next:
                
                return 1 + list_len(head.next)
            
            else:
                
                return 1
            
        def get_nodes(i:int):
            # O(N)
            # cur_node = head
            
            # while i!=0:
                
                # cur_node = cur_node.next
                # i-=1
                
            # return cur_node
            
            # O(1)
            
            tmp = head
            
            return eval(f"tmp{'.next'*i}")
            
        
                
            
            
        n = list_len(head)
        
        
        steps_to_left_target = k - 1
        
        steps_to_right_target = n - k
        
        
        
        left_node, right_node = get_nodes(steps_to_left_target), get_nodes(steps_to_right_target)
        
        
        left_node.val, right_node.val = right_node.val, left_node.val
        
        return head
        
        
        
        
        
        