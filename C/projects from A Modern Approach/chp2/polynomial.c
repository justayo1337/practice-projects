#include <stdio.h>


int main(){

    float A,B,C,D,E;
    float x,final;
    printf("Please enter the value for x: ");
    scanf ("%f", &x);
    A = 3 * x * x * x * x * x;
    B = 2 * x * x * x * x ;
    C = 5 * x * x * x;
    D = x * x;
    E = 7 * x ;

    final = A + B - C - D + E - 6;

    printf("The result is: %f", final);
    return 0;
}