#include <stdio.h>


int main(){
    int num1,denom1,num2,denom2,result_num,result_denom;
    
    printf("Enter the two fractions separated by a plus sign: ");
    scanf("%d/%d+%d/%d",&num1,&denom1,&num2,&denom2);

     
    result_denom = denom1*denom2;
    result_num = (num1 * denom2) + (num2 * denom1);

    printf("The sum is: %d/%d",result_num,result_denom);
    return 0;
}