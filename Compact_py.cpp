Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
In this problem, a substring is defined as a sequence of continuous characters Si, Si+1, ..., Sj where 1 ≤ i ≤ j ≤ N.

Input
First line contains T, the number of testcases. Each testcase consists of N(the length of string) in one line and string in second line.

Output
For each testcase, print the required answer in one line.

Constraints
1 ≤ T ≤ 105
1 ≤ N ≤ 105
Sum of N over all testcases ≤ 105
Example
Input:
2
4
1111
5
10001

Output:
10
3
Explanation
#test1: All substrings satisfy.
#test2: Three substrings S[1,1], S[5,5] and S[1,5] satisfy.

It's c++ solution:

#include <bits/stdc++.h> 
using namespace std;
long long l=0, t=0, n=0;
string s;
int main(){
  cin>>t;  
  for(long long i=1; i<=t; i++){
     long long cnt=0; 
     cin>>n;
     cin>>s;
     l = s.length();
     char arr[n+1];
     strcpy(arr, s.c_str());
     cnt = count(arr, arr + n, '1');
     cout<<cnt*(cnt+1)/2<<endl;
     }
  }    
  
It's python solution:

for i in range(int(input())):
    n=int(input())
    s=input()
    cnt=s.count('1')
    print(cnt*(cnt+1)//2)
    
Note: Both the code have the same functionality !
Python is really compact
    
