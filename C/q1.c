#include <stdio.h>


void printArr(int arr[], int n);
void reverseOrder(int arr[], int n);

int main()
{
    int size = 11;
    int arr[size];
    for (int i = 0; i < size; i++)
    {
        arr[i] = i+1;
    }
    printArr(arr, size);
    reverseOrder(arr, size);
    printArr(arr, size);
    return 0;
}

void printArr(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%i, ", arr[i]);
    }
    printf("\n");
}

void reverseOrder(int arr[], int n)
{
    for(int i = 0; i < n; i++)
    {
        if(i >= n/2)
            break;
        
        int swap = arr[n-1-i];
        arr[n-1-i] = arr[i];
        arr[i] = swap;
    }
}