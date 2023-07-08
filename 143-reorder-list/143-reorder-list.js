/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    
    let order = [];
    let node = head;
    while(node !== null){
        order.push(node.val);
        node = node.next;
    };
    
    let left = 0;
    let right = order.length - 1;
    
    while(left <= right){
        if(left != right){
            head.val = order[left];
            head.next.val = order[right];
            right -- ;
            left ++ ;
            head = head.next.next
        }else{            
            head.val = order[left];
            return
        }
    }
    
};