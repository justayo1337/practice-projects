#include <stdio.h>
#include <stdlib.h>

/* aim of the program is to print out fahrenheit-celcius table up to 200 degrees fahrenheit*/

int main(){

    signed int fahr, celc;
    int lower = 0, upper = 300,step = 20;

    printf("F  |  C\n");
    for (fahr = lower; fahr <= upper;fahr+= step){
        celc = (5 * (fahr - 32))/9;
        //printf("%d", celc);
        printf("%d  |  %d\n",fahr,celc);
        
    }
    return 0;
}


