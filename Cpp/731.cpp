/*Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.*/

#include <iostream>
#include <climits>
using namespace std;

int processArray(int *arr, int size);
void parseArray(int *arr, int i, int j, int *max_val);

int main()
{

    int size;
    scanf("%d",&size);
    int arr[size];
    for(int i =0 ; i < size; ++i)
    {
        scanf("%d",&arr[i]);
    }
    processArray(arr,size);
    return 0;
}

int processArray(int *arr, int size)
{
    int max_val = INT_MIN;
    parseArray(arr,0,size - 1,&max_val);
    printf("Ans: %d\n",max_val);
}

void parseArray(int *arr, int i, int j, int *max_val)
{
    //base condition
    if(i >= j)
    {
        return;
    }
    
    //calculate the difference    
    int diff = arr[j] - arr[i];
    if(*max_val < diff)
    {
        *max_val = diff;
    }
    
    //Two paths
    parseArray(arr,i + 1, j ,max_val);
    parseArray(arr,i,j - 1,max_val);
}
