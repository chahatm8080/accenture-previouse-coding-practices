#include<bits/stdc++.h>
using namespace std;
int maximum_Subarrays(int arr[],n)
{
  int sum =0;
  for(i=0;i<n;i++)
  {
    sum+=arr[i];
    max=max(max,sum);
    if(sum<0)
    {
      sum=0;
    }
  }
  return sum;
}
int main ()
{
  int arr[]={-2,1,-3,4,-1,2,1,-5,4};
  int n=sizeof(arr)/sizeof(arr[0]);
  cout<<maximum_Subarrays(arr);
}