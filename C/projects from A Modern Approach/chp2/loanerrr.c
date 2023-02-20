#include <stdio.h>


int main(){
// declare vars

    float amount,rate,monthly_payments;
    float first,second,third;

    printf("Enter amount of loan: ");
    scanf("%f", &amount);

    printf("Enter interest rate: ");
    scanf("%f", &rate);

    printf("Enter monthly payment: ");
    scanf("%f", &monthly_payments);

    float monthly_rate = rate / 1200.0f;

    first = (amount - monthly_payments) + ((amount - monthly_payments) * monthly_rate);
    second = (first - monthly_payments) + ((first - monthly_payments) * monthly_rate);
    third = ( second - monthly_payments) + ((second - monthly_payments) * monthly_rate);


    printf("Balance remaining after first payment: $%.2f\nBalance remaining after second payment: $%.2f\nBalance remaining after third payment: $%.2f\n",first,second,third);

    return 0;
}