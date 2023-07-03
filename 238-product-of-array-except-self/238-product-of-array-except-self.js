/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    
    let sum = 1
    let tmp = []
    let ziros = []
    
    for(let i in nums){
        if (nums[i] == 0){
            ziros.push(i)
        }else{
            sum *= nums[i]
        }
    };
    
    if(ziros.length > 1 || ziros.length == nums.length){
        return new Array(nums.length).fill(0)
    }
    
    for(let i in nums){
        
        if(ziros.length > 0){
            
            if(nums[i] == 0){
                tmp.push(sum)
            }else{
                tmp.push(0)
            }
        }else{
            tmp.push(sum/nums[i])
        }
    }
    return tmp
    
    
};