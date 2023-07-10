class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        # I have focused on space comp and complitly forgot about time comp
        
        out_head = ListNode()
        out_node = out_head
        k = len(lists)
        
        while any(lists):
            
            min_node = ListNode(float('inf'))
            idx = -1
            
            for i, node in enumerate(lists):
                if node and node.val < min_node.val:
                    min_node = node
                    idx = i
            
            if idx == -1:
                break
            
            out_node.next = min_node
            out_node = out_node.next
            
            lists[idx] = lists[idx].next
            
            if not lists[idx]:
                del lists[idx]
            
        return out_head.next
