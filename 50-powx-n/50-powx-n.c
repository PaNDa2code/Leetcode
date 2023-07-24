bool isOdd(int x){
    return x % 2 != 0;
};

double myPow(double x, long long n){
    if (n == 0){
        return 1.0;
    };
    if (n < 0){
        return 1.0 / myPow(x,-1*n);
    };
    
    if(isOdd(n)){
        return x * myPow(x*x,(n-1)/2);
    }else{
        return myPow(x*x,n/2);
    };
};