int findMin(int* nums, int numsSize){
    
    int left = 0;
    int right = numsSize - 1;
    
    int mid;
    
    while(left < right){
      
        mid = floor((double)(left+right) / 2);
        
        if(nums[mid] > nums[right]){
            left = mid + 1;
        }else if(nums[mid] < nums[right]){
            right = mid;
        }else{
            right --;
        };
    
    };
    return nums[left];
};