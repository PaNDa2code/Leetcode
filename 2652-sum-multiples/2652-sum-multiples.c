#include <stdio.h>
int sumOfMultiples(int n){
    // Write C code here
    int sum = 0 ;
    int i;
    
    for(i=1;i <= n; i++){
        if(i % 3 == 0 || i % 5 == 0 || i % 7 == 0){
            sum = sum + i;
            
        }
    };
    return(sum);

}