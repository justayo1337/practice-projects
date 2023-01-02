#include <stdio.h>
#include <stdlib.h>
#define MAX 10000

//function to append the 

int fib(int *arr, int num){
if (num == 0 ){
    return 0;
}else {
    for (int i = 0; i < num ; ++i){
        if (i == 0){
            arr[i] = 0;
        }else if(i== 1){
            arr[i] = 1; 
        }else {
            arr[i] = arr[i-1] + arr[i-2];
        }}}
 return 0;   
}

int main(int argc, char *argv[]){
    int arr[MAX];
    int n = atoi(argv[1]);
    fib(arr,n);
    printf("The numbers are: ");
    for (int i = 0; i < n; ++i){
        printf("%d ",arr[i]);
    
    }
    return 0;
}
