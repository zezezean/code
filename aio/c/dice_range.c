#include <stdio.h>
int main(void){
    int a,b;
    printf("Enter the number of sides on your dice: ");
    scanf("%i",&a);
    printf("Enter the number of dice being rolled: ");
    scanf("%i",&b);
    if(a<=0||b<=0){
        printf("These dice will not produce a range.");
    }
    else{
        float f=(a+b)/2;
        printf("Your dice range is %i to %i.\nThe average value is %f",b,a*b,f);
    }
    return 0;
}