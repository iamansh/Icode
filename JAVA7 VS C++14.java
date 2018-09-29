https://www.codechef.com/problems/LAPIN

JAVA:-

import java.util.*;
class A{
    public static void isLapin(String s){
         char ch1[] = new char[100];
         char ch2[] = new char[100];
        int n = s.length();
        int iter = n/2;
        int iter2 = iter;
        if(n%2!=0)
            iter2++;
        String s1 = s.substring(0, iter);
        String s2 = s.substring(iter2, n);
        ch1= s1.toCharArray();
        ch2 = s2.toCharArray();
        Arrays.sort(ch1);
        Arrays.sort(ch2);
        if(Arrays.toString(ch1).equals(Arrays.toString(ch2)) )
            System.out.println("YES");
        else
            System.out.println("NO");
    }
      
    public static void main(String[] x){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while(T-->0){
            String s = sc.next();
            A.isLapin(s);
        }
    }
}

Execution time: 0.02s

C++14:-

#include<iostream>
#include<cctype>
#include<cstring>
#include<algorithm>
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
    s1==s2?cout<<"YES"<<endl:cout<<"NO"<<endl;
    
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
   Execution time: 0.00s
   
 Pyhton 3.6:-
     
def isLapin(s):
    n, s1, s2 = len(s), [], []
    iter = n//2
    iter2 = iter
    for j in range(0, iter):
        s1.append(s[j])
    if n%2!=0:
        iter2+=1
        for j in range(iter2, n):
            s2.append(s[j])
    else:
        for j in range(iter2, n):
            s2.append(s[j])
    s1.sort()
    s2.sort()
    if(s1==s2):
        print("YES")
    else:
        print("NO")
        

T = int(input())
for i in range(0, T):
    s = list(input())
    isLapin(s)
        
Execution time: 0.04s        
