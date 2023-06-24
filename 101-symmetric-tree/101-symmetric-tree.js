/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    
    const p = function(node1,node2){
        
        if(node1 == null & node2 == null){
            return true
        }
        else if(node1 == null | node2 == null){
            return false
        }
        else if(node1.val != node2.val){
            return false
        };
        return p(node1.left,node2.right) & p(node1.right,node2.left)
    };
    return p(root.left,root.right)
    
};