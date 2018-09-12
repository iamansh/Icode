                                                          MESSY THING!
 Consider the following question on codechef:
 https://www.codechef.com/problems/BROKPHON
 
 As usual I wrote an answer for it:
 
 #include<iostream>
 int a[112345];
 using namespace std;
 int main(){
   int N, T;
   cin>>T;
   while(T--){
   cin>>N;
   if(N==1){
     cout<<0<<endl;
     continue;
   }
   for(int i=1; i<=N; i++){
     cin>>a[i];
     M = a[1];
     if(M == a[1])
       continue;
     if(M != a[i]){
       cout<<N-i<<endl;
       break;
       }
  }
}
My code's logic is cakewalk having no malfunction and complexity of O(n).
But it shows TLE!

Here is another code which is far more complex and having O(n^2) complexity, but it's lack of TLE!

#include <iostream>
using namespace std;
// allocate more than necessary
int A[112345];
int main() {
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        // we use 'cas' because 'case' is a keyword
        int N;
        cin >> N;
        int count = 0;
        for (int i = 1; i <= N; i++) {
            cin >> A[i];
        }
        for (int i = 1; i <= N; i++) {
            if(i > 1){
                if(A[i] != A[i - 1]){
                    count++;
                    continue;
                }
            }
            if(i < N){
                if(A[i] != A[i + 1]){
                    count++;
                }
            }
        }
        cout << count << '\n';
    }
}
       
       
       HOW??
       
