/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    
    let sum = 1
    let tmp = []
    let zeros = []
    
    for(let i in nums){
        if (nums[i] == 0){
            zeros.push(i)
        }else{
            sum *= nums[i]
        }
    };
    
    if(zeros.length > 1 || zeros.length == nums.length){
        tmp = Array(nums.length).fill(0)
        return tmp
    }else if(zeros.length == 1){
        tmp = Array(nums.length).fill(0)
        tmp[zeros[0]] = sum
        return tmp
    }else{
        for(let num of nums){
            tmp.push(sum/num)
            
        };
        return tmp
    }
    
    
    
    
};