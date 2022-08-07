#include <stdio.h>

double y(int n){

    if(n<0){
        return 0;
    }
    if(n>=0){
        return (double)-1/2*y(n-1)+x(n)+x(n-2);
    }
}

int x(int n){
    int x_arr[]={1,2,3,4,2,1};
    if(n<0||n>=6){
        return 0;
    }
    else{
        return x_arr[n];
    }
}

int main(){

    // float y[10];
    // y[0]=x[0]
    // y[1]=-1/2*y[0]+x[1]



for(int i=-5;i<10;i++){
printf("%f ",y(i));

}
    return 0;
}