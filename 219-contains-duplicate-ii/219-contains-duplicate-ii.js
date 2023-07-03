/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    
    const hashmap = new Map();
    
    for(let i in nums){
        num = nums[i]
        
        if(hashmap.has(num)){
            if(Math.abs(i-hashmap.get(num)) <= k){
                return true
            }
        }
        hashmap.set(num,i)
    };
    return false
    
};