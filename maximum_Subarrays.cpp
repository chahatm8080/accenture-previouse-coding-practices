#include<bits/stdc++.h>
using namespace std;
int maximum_subarrays(int arr[],int n)
{
  int res=INT_MIN;
  int current_sum=0;
  for (int i=0;i<n;i++)
  {
    current_sum += arr[i];
    res = max(current_sum, res);
    if(current_sum<0)
    {
      current_sum=0;
    }
  }
}
int main()
{
  int arr[]={10,20,3,4,5,6};
  int n=sizeof(arr)/sizeof(arr[0]);
  cout<<maximum_subarrays(arr,n);
}