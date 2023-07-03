/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    const hashmap = new Map;
    
    for(let num of nums){
        num = num.toString()
        if(hashmap.has(num)){
            return true
        };
        hashmap.set(num,1)
        
    };
    return false
};