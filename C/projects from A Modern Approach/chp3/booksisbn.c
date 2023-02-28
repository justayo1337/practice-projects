#include <stdio.h>



int main(){

    int gsi,group,pub,item,check;
    printf("Enter ISBN: ");
    scanf("%d-%d-%d-%d-%d",&gsi,&group,&pub,&item,&check);


    printf("GS1 prefix: %d\nGroup Identifier: %d\nPublisher code: %d\nItem number: %d\nCheck digit: %d\n",gsi,group,pub,item,check);
    return 0;
}