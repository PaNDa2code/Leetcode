/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    
    if(typeof list1 === 'undefined' && typeof list2 === 'undefined'){
        return
    }else if(list1 === null){
        return list2
    }else if(list2 === null){
        return list1
    };
    
    let out = new ListNode();
    let node= out;
    
    while(list1 !== null && list2 !== null){
        
        if(list1.val <= list2.val){
            node.val = list1.val;
            list1 = list1.next;
        }else{
            node.val = list2.val;
            list2 = list2.next
        };
        
        if(list1 !== null && list2 !== null){
            node.next = new ListNode();
            node = node.next;
        }
        
        
    }
    
    if(list1 !== null){
        node.next = list1;
    }else if(list2 !== null){
        node.next = list2;
    }
    return out
    
};