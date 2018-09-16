Codechef problem:
https://www.codechef.com/problems/TWTCLOSE

Solution in python:

n, q = map(int, input().split())
l = [0]*1010
for i in range(0, q):
    s = input()
    if s in "CLICK":
        t = int(input())
        l[t]^=1
    else:
        l = [0]*n
    c = 0
    for i in range(1, n+1):
       c+=l[i]
    print(c)       
    
    Solution in java:
    
 import java.util.*;
class PQ{
 public static void main(String []x){
 int n, q, t=0, c;
 int a[] = new int[1010];
 Scanner sc = new Scanner(System.in);
 n = sc.nextInt(); q = sc.nextInt(); Arrays.fill(a, 0);
 while((q--)>0){
       String s = sc.next();
       if(s.equals("CLICK")){ 
         t = sc.nextInt();
         a[t]^=1;
       }
       else Arrays.fill(a, 0);
       c=0;
       for(int i=1; i<=n; i++)  c+=a[i];        
       System.out.println(c);
       }
    }
} 
