#include <stdio.h>
#include <math.h>

void isPrime(int n);

int main(){
    int num;
    
    printf("Please ent an integer >= 2; Enter q to quit.\n");
    

    while(1)
    {
        int r = scanf("%i", &num);
        if(r!=1)
        {
            break;
        }
        if(num < 2)
        {
            printf("Try again.\n");
            continue;
        }
        isPrime(num);
        printf("Please enter another integer >= 2; Enter q to quit.\n");
    }
    printf("Bye.\n");
}

void isPrime(int n)
{
    int prime = 1;
    for(int i = 2; i < n; i++)
    {
        if(i > sqrt(n))
            break;
        if(n % i == 0)
        {
            prime = 0;
            if(i == n/i)
            {
                printf("%i is divisible by %i.\n", n, i);
            }
            else
            {
                printf("%i is divisible by %i and %i.\n", n, i, n/i);
            }
        }
    }
    if(prime==1)
    {
        printf("%i is prime.\n", n);
    }
}
