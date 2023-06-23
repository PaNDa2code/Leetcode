/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    
    const preorder_t = function(node){
        
        if(node != null){
         return [node.val].concat(preorder_t(node.left),preorder_t(node.right))   
        }
        else{
            return ['null']
        };
        
    };
    
    return JSON.stringify(preorder_t(p)) === JSON.stringify(preorder_t(q));
    
};