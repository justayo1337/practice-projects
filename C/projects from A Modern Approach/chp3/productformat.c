#include <stdio.h>


int main(){
    int num;
    float price;
    char date[9];
    printf("Enter item number: ");
    scanf("%d",&num);

    printf("Enter unit price: ");
    scanf("%f",&price);

    printf("Enter Purchase date: ");
    scanf("%s",&date);

    printf("Item        Unit Price        Purchase Date\n%-d        $%.3f       %-s",num,price,date);

    return 0;
}