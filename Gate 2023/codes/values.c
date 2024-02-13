#include<stdio.h>

int main(){
    FILE *fptr=fopen("values.dat", "w");
    float y[2000]={};
    float dx=(5.01)/1000;
    for(int i=1; i<1000; i++){
        y[1000+i]=-4*i*dx-2/(i*dx);
        y[999-i]=4*i*dx+2/(i*dx);
    }
    y[999]= 200;
    y[1000]=-200;

    for(int i=0; i<1999; i++) fprintf(fptr, "%f ", y[i]);
    fprintf(fptr, "%f", y[1999]);
}