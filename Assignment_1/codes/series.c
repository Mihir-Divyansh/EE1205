#include<stdio.h>
#include<math.h>

int main(){
    FILE *ptr;
    ptr= fopen("series.txt", "w");
    float x_0=1/256.0;
    float r= 2;
    for(int i=0; i<16; i++){
        fprintf(ptr, "%f ", x_0*pow(r,i));
    }
    fprintf(ptr,"%f\n", x_0*pow(r,16));
}