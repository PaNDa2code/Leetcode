/**
 * @param {number[]} nums
 * @return {number[]}
 */
// var productExceptSelf = function(nums) {
    
//     let sum = 1
//     let tmp = []
//     let zeros = []
    
//     for(let i in nums){
//         if (nums[i] == 0){
//             zeros.push(i)
//         }else{
//             sum *= nums[i]
//         }
//     };
    
//     if(zeros.length > 1 || zeros.length == nums.length){
//         tmp = Array(nums.length).fill(0)
//         return tmp
//     }else if(zeros.length == 1){
//         tmp = Array(nums.length).fill(0)
//         tmp[zeros[0]] = sum
//         return tmp
//     }else{
//         for(let num of nums){
//             tmp.push(sum/num)
            
//         };
//         return tmp
//     }
    
    
    
    
// };

var productExceptSelf = function(nums) {
    
    const n = nums.length;
    let output = new Array(n).fill(1);
    
    var prefix_product = 1;
    
    for(let i = 0;i < n;i++){
        output[i] *= prefix_product;
        prefix_product *= nums[i]
    };
    
    var suffix_product = 1;
    
    for(let i = n-1; i >= 0; i--){
        output[i] *= suffix_product ;
        suffix_product *= nums[i]
    };
    
    return output
}