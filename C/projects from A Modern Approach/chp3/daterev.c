#include <stdio.h>


int main(){

    int mm,dd,yyyy;

    printf("Enter Day in the form mm/dd/yyyy: ");

    scanf("%d/%d/%d",&mm,&dd,&yyyy);

    printf("You entered the date: %0.2d/%0.2d/%0.2d\n",yyyy,mm,dd);
    return 0;
}