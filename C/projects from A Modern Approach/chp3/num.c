#include <stdio.h>



int main(){
    int one,two,three,four;
    int five,six,seven,eight;
    int nine,ten,eleven,twelv;
    int thirteen,fourtee,fifteen,sixteen;
    int row_sums,col_sums,diag_sums;


    printf("Enter the numbers from 1 to 16 in any order: ");

    scanf("%d%d%d%d",&one,&two,&three,&four);
    scanf("%d%d%d%d",&five,&six,&seven,&eight);
    scanf("%d%d%d%d",&nine,&ten,&eleven,&twelv);
    scanf("%d%d%d%d",&thirteen,&fourtee,&fifteen,&sixteen);

    printf("%d %d %d %d\n%d %d %d %d\n%d %d %d %d\n%d %d %d %d\n",one,two,three,four,five,six,seven,
    eight,nine,ten,eleven,twelv,thirteen,fourtee,fifteen,sixteen);

    printf("Row sums: %d %d %d %d\nColumn Sums: %d %d %d %d\nDiagonal sums: %d %d",(one+two+three+four),
    (five+six+seven+eight),(nine+ten+eleven+twelv),(thirteen+fourtee+fifteen+sixteen),(one+five+nine+thirteen),
    (two+six+ten+fourtee),(three+seven+eleven+fifteen),(four+eight+twelv+sixteen),(one+six+eleven+sixteen),(four+seven+ten+thirteen));

    return 0;
}