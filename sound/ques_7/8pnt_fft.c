#include <stdio.h>
#include <math.h>
#include <complex.h>


 complex W(int N,int k){
    return cos((float)(2*M_PI*k)/N)-I*sin((float)(2*M_PI*k)/N);

}

 complex FFT(int N,int k,int x[]){

    if(N%2==0){
        int x1[N/2],x2[N/2];
        for(int i=0;i<N;i++){
            if(i%2==0)x1[i/2]=x[i];
            else x2[(i-1)/2]=x[i];
        }
        
        
        return FFT(N/2,k,x1)+W(N,k)*FFT(N/2,k,x2);
    }
    else if(N==1){
        return x[0];
    }
    else{
        printf("can't find FFT");
        return ;
    }
}
int main(){
    
    int x[]={1,2,3,4,2,1,0,0};
    int N=8;
    complex X[N];
    int t=20;
    int time[t];

    // for(int j=0;j<t;j++){
    //     int clock=clock();
    // for(int i=0;i<N;i++){
    //     X[i]=FFT(N,i,x);
    //     printf("%lf %lf \n",creal(X[i]),cimag(X[i]));
    // }
    // }
    printf("%lf %lf %lf %lf %lf %lf\n",creal(W(8,1)),cimag(W(8,1)),creal(W(8,2)),cimag(W(8,2)),creal(W(8,3)),cimag(W(8,3)));
    return 0;

}
