Here is the question...
https://www.codechef.com/SEPT18B/problems/XORIER

When I solved with java, 2.02 seconds did it takes for execution:

import java.util.*;
class GFG{
   static int findPrimePair(int A[], int N){
       int R=0, i=1, j=2, c=0;
       for(; j<=N; j++){
                R = A[i]^A[j];
                if(R%2==0 && R>2)
                    c++;
                if(j==N-1){
                  i++; 
                  j=i; 
                  continue;
                }
       }
       return c;
   }

 
public static void main (String[] args) 
    {   
        Scanner sc  = new Scanner(System.in);
        int T = sc.nextInt(); 
        int i, N;
        while((T--)>0){
         N = sc.nextInt();
         int A[] = new int[N];
         for(i=1; i<=N; i++)
            A[i] = sc.nextInt();

            System.out.println(GFG.findPrimePair(A, N));
            System.out.println();
                   
                }             
         }
  }
       
   But when I used c++, time get reduced considerably (1.01)seconds. !
   How, it becomes a nightmare for me which protecting itself to buried on..
   
   #include<iostream>
   using namespace std;

    int findPrimePair(int A[], int N){
       int R=0, i=0, j=0;
       for(i=0; i<N-1; i++)
            for(j=i+1; j<N; j++){
                R = A[i]^A[j];
                if(R%2==0 && R>2)
                    c++;
       }
       return c;
   }
int main () 
    {   
        int T;
        cin>>T; 
        int N;
        while(T--){
         cin>>N;
         int Arr[N];
         for(int i=0; i<N; i++)
            cin>>A[i];

            cout<<findPrimePair(A, N)<<endl;  
                   
                }             
         }
       
