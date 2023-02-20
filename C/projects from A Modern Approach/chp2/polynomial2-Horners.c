#include <stdio.h>


int main(){

    float A,B,C,D,E;
    float x,final;
    printf("Please enter the value for x: ");
    scanf ("%f", &x);
    A = (3 * x) + 2;
    B = (A * x) - 5;
    C = (B * x) - 1;
    D = (C * x) + 7;
    E = D * x ;

    final =  E - 6;

    printf("The result is: %f", final);
    return 0;
}