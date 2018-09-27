Here is the question..
https://www.codechef.com/problems/NUKES

Hi! As is clearly evident, if you go about solving the problem the naive way, 
it would create a horrendously messy code. 

#include<iostream>
using namespace std;
int main(){
 int A, N, K;
 cin>>A>>N>>K;
 int k[K], a[A];
 Arrays.fill(K, 0);
 Arrays.fill(a, 1);
 if(N >= A)
   for(int i=1; i<=K; i++){
     if(i==1){
       cout<<A;
       continue;}
     cout<<0;  
     }
  else if(N < A){
   for(int i=1; i<=K; i++)
     if(A!=0)
       A-=1;
       k[i] += a[i];
       k[i-1] = 0;
       if(k[i]>N){
         k[i]=0;
         continue;}
         
    The above one is naive, as I did!
    
    If you look over the actual solution, you'll gonna deprecate my head.
    
#include <iostream>
using namespace std;
int main() { 
 int a, n, k;
 cin>>a>>n>>k;
 while(k--) {
  cout<<a%(n+1)<<" "; a=a/(n+1);
 }
 return 0;
}
       
       
