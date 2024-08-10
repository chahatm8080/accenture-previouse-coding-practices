#include <bits/stdc++.h>
using namespace std;
int reverse(int n)
{
  int reverse=0;
  while (n != 0)
  {
    int r = n % 10;
    reverse = reverse*10+r;
    n=n/10;
  }
  return reverse;
}
int main()
{
  int n = 123456;
  int rev = reverse(n);
  cout << "reverse of number is : "<< rev<<endl;
}