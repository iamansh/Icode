question:https://www.codechef.com/problems/LAPIN

what's the error in the below code:

#include<iostream>
#include<cctype>
using namespace std;
int cntL[100], cntR[100];
bool isLapin(string s){
    int n = s.length();
    for(int i=0; i<n/2; i++)
      cntL[s.at(i)-'a']++;
    for(int i=n/2; i<n; i++)
      cntR[s.at(i)-'a']++;
    bool r = true;
    for(int i=0; i<26; i++)
      if(cntL[i] != cntR[i])
        r = false;
    return r;        
}


int main(){
    int T;
    cin>>T;
    while(T--){
      string s;
      cin>>s;
      cout<<isLapin(s)<<endl;
    }
}
   
