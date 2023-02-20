#include <stdio.h>
 
#define PI 3.142

int main(){

    int r = 10;

    float vol = 4/3.0f * r * r * r * PI;
    printf("The volume is:  %f", vol);

    return 0;
}