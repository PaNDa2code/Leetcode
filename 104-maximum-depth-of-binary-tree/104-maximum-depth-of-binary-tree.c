/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root){
    
    if(root == NULL){
        return 0;
    };
    
    int left = 1 + maxDepth(root->left);
    int right = 1 + maxDepth(root->right);
    
    if (left >= right){
        return left;
    }else{
        return right;
    };

}