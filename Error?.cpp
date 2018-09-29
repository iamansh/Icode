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
   
Ok! ok!, don't do such mess with that. Here is the awesome one:-)
    
#include<iostream>
#include<cctype>//toupper()
#include<cstring>
#include<algorithm>//sort()
using namespace std;
int cntL[100], cntR[100];

void isLapin(string s){
    int n = s.length();
    int iter = n/2;
    int iter2 = iter; //if even
    if(n%2)
      iter2++;// if odd then increase iter by one
    string s1 = s.substr(0, iter);
    string s2 = s.substr(iter2, n);
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    if(s1 == s2)
        cout<<"YES"<<endl;
    else 
        cout<<"NO"<<endl;
    
}

int main(){
    int T;
    cin>>T;
    while(T--){
      string s;
      cin>>s;
      isLapin(s);
    }
}
   
