#include <stdio.h>

int main(){
    int dolla,tw,t,five,one,remainder;

    printf("Enter a dollar amount: ");
    scanf("%d", &dolla);

    tw = dolla / 20;
    remainder = dolla % 20;

    t = remainder / 10;
    remainder = remainder % 10;

    five = remainder / 5;
    remainder = remainder % 5;

    one = remainder / 1;
    remainder = remainder % 1;

    printf("$20 bills: %d\n$10 bills: %d\n$5 bills: %d\n$1 bills: %d\n", tw,t,five,one);
    return 0;
}