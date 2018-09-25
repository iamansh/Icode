#include<iostream>
using namespace std;
int main(){
  int T, i=0, j=0, f=0;
  cin>>T;  
  while(T--){
   string str;
   cin>>str; 
  int n = str.length();
   for(i=0, j=n; i<int(n/2); i++, j--){
      if(str.at(i) == str.at(j))
        continue;
      else if(str.at(i) != str.at(j)){
        f=1;
        break;}
    }
    if(f==1)
      cout<<"palindrome";
    else if(f==0)
      cout<<"Not";
     }
  }
