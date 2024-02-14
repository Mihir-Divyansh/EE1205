#include<stdio.h>

int main(){
    FILE *fptr=fopen("values.dat", "w");
    float y[200]={};
    float dx=(5.01)/100;
    for(int i=1; i<100; i++){
        y[100+i]=-4*i*dx-2/(i*dx);
        y[99-i]=4*i*dx+2/(i*dx);
    }
    y[99]= 60;
    y[100]=-60;

    for(int i=0; i<199; i++) fprintf(fptr, "%f ", y[i]);
    fprintf(fptr, "%f", y[199]);
}