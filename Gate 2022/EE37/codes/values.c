#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SIZE 10000

//linspace function
float* linspace(float start, float end, int stepNum){
    float* array=(float*)malloc(stepNum*sizeof(int));
    float dx= (end-start)/stepNum;
    //Filling the array with evenly-spaced values
    for (int i=0; i<stepNum; i++){
        array[i]=start+dx*i;
    }
    return array;
    free(array);
}
//function to generate the values of transfer function
float* H(float* s){
    float* transfer=(float*)malloc(SIZE*sizeof(float));
    for(int i=0; i<SIZE; i++){
        transfer[i]=(float)1.0/((float)pow((s[i]),2)+(float)(0.1*s[i]+10));
    }
    return transfer;
    free(transfer);
}
//function to generate values of output of the system
float* y(float* t){
    float* output=(float*)malloc(SIZE*sizeof(float));
    for (int j=0; j<SIZE; j++){
        output[j]=10+sin(10*t[j]+0.0111106539);
    } 
    return output;
    free(output);
}
//function to generate values of the input of the system
float* x(float* t){
    float* input=(float*)malloc(SIZE*sizeof(float));
    for (int l=0;l<SIZE; l++){
        input[l]=1+0.1*sin(10*t[l]);
    } 
    return input;
    free(input);
}
int main(){
    FILE *fp=fopen("data.dat", "w");
    float* t=linspace(-5,5,SIZE);
    float* s=linspace(-10,10, SIZE);
    //printing values to dat file
    for(int k=0; k<SIZE;k++){
        fprintf(fp, "%f\t%f\t%f\n", (x(t))[k], (y(t))[k], (H(s))[k]);
    }
    free(t);
    free(s);
}