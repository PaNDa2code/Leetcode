/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

var gitMid = function(left,right){
    return Math.floor((left+right)  / 2);
};
var search = function(nums, target) {
    
    left = 0;
    right = nums.length;
    if (!nums.includes(target)) {
        return -1;
    }
    while(left <= right){
        mid = gitMid(left,right);
        mid_f = nums[mid];
        if(mid_f < target){
            left = mid + 1
        }
        else if (mid_f > target){
            right = mid - 1
        };
        if (mid_f == target){
            return mid
        }
    };
    
};
