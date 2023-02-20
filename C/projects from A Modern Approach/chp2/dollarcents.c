#include <stdio.h>


int main(){

    float tax,total,cap;
    printf("Please input your dollar cent amount(e.g 100.00): ");
    scanf("%f", &cap);

    tax = 0.05 * cap;
    total = tax + cap;

    printf("With tax added: %f", total);
    return 0;
}