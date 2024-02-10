#include<stdio.h>

int main(){
    FILE *ptr=fopen("series.dat", "w");
    int x_0=-32, d=7;
    for(int i=0; i<32; i++) fprintf(ptr, "%d ", (x_0+7*i));
    fprintf(ptr, "%d", x_0+7*32);
    return 0;
}