#include <stdio.h>
int findMax(int a, int b) {
    return (a > b) ? a : b;
}
int maximumCount(int* nums, int numsSize){
    int neg = 0;
    int pos = 0;
    int i;
    for(i=0;i < numsSize;i++){
        int n = nums[i];
        if (n < 0){
            neg ++;
        }
        else if (n > 0){
            pos ++;
        };
    };
    
    return findMax(neg,pos);

};