#include <stdio.h>
 
#define PI 3.142

int main(){

    float r;

    printf("Enter the radius: ");

    scanf("%f", &r);

    float vol = 4/3.0f * r * r * r * PI;
    printf("The volume is:  %f", vol);

    return 0;
}