There was a question in september challenge :
https://www.codechef.com/SEPT18B/problems/CHEFADV

The below code is perfect and shows correct o/p for each and evey queries when compiled on local compiler:
But when on codechef complier, uncanny!

#include<iostream>
using namespace std;
int T;
long int N, M, X, Y;
int main(){
cin>>T;
while(T--){
  cin>>N>>M>>X>>Y;
   if((N%X==2 && M%Y==2) || (N%X==0 && M%Y==0) || (N%X==1 && M%Y==1)){
      cout<<"Chefirnemo"<<endl;
      continue;
    }
    else cout<<"Pofik"<<endl;
  }
 } 
    
 I bet if anyone can point out the error!   
