#include<iostream>
using namespace std;
string reversed(string s){
    string reverse_str=" ";
    for(int i=0;i<s.size();i++)
    {
      reverse_str=s[i]+reverse_str;
    }
  return reverse_str;
}
int main ()
{
  int n;
  string s= "hello";
  cout<<"reverse of string is :"<<reversed(s);
}