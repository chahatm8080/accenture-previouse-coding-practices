#include<bits/stdc++.h>
using namespace std;
int largest(int arr[],int n)
{
  int large=arr[0];
  for (int i=1;i<n;i++)
  {
    if(arr[i]>large)
    {
      large=arr[i];
    }
  }
  return large;
}
int main()
{
  int arr[]={19,24,56,64,4};
  int n=sizeof(arr)/sizeof(arr[0]);
  cout<<largest(arr,n);
}