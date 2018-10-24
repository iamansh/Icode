For solving this question, one needs to know the Euler's totient function:(GEEKSFORGEEKS)

Euler’s Totient Function
Euler’s Totient function ?(n) for an input n is count of numbers in {1, 2, 3, …, n} that are relatively 
 prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.
Examples :

?(1) = 1  
gcd(1, 1) is 1

?(2) = 1
gcd(1, 2) is 1, but gcd(2, 2) is 2.

?(3) = 2
gcd(1, 3) is 1 and gcd(2, 3) is 1

?(4) = 2
gcd(1, 4) is 1 and gcd(3, 4) is 1

?(5) = 4
gcd(1, 5) is 1, gcd(2, 5) is 1, 
gcd(3, 5) is 1 and gcd(4, 5) is 1

?(6) = 2
gcd(1, 6) is 1 and gcd(5, 6) is 1, 

  
int gcd(int a, int b) 
{ 
    if (a == 0) 
        return b; 
    return gcd(b % a, a); 
} 
  

int Euler(unsigned int n) 
{ 
    unsigned int result = 1; 
    for (int i = 2; i < n; i++) 
        if (gcd(i, n) == 1) 
            result++; 
    return result; 
} 
  

int main() 
{ 
    int n; 
    for (n = 1; n <= 10; n++) 
        printf("Euler(%d) = %d\n", n, Euler(n)); 
    return 0; 
} 


#include <bits/stdc++.h> 
using namespace std; 
#define N 100005 
  
// to store euler's totient function 
int phi[N]; 
  
// to store required answer 
int S[N]; 
  
// Computes and prints totient of all numbers 
// smaller than or equal to N. 
void computeTotient() 
{ 
    // Initialise the phi[] with 1 
    for (int i = 1; i < N; i++) 
        phi[i] = i; 
  
    // Compute other Phi values 
    for (int p = 2; p < N; p++) { 
  
        // If phi[p] is not computed already, 
        // then number p is prime 
        if (phi[p] == p) { 
  
            // Phi of a prime number p is 
            // always equal to p-1. 
            phi[p] = p - 1; 
  
            // Update phi values of all 
            // multiples of p 
            for (int i = 2 * p; i < N; i += p) { 
  
                // Add contribution of p to its 
                // multiple i by multiplying with 
                // (1 - 1/p) 
                phi[i] = (phi[i] / p) * (p - 1); 
            } 
        } 
    } 
} 
  
// function to compute number coprime pairs 
void CoPrimes() 
{ 
    // function call to compute 
    // euler totient function 
    computeTotient(); 
  
    // prefix sum of all euler totient function values 
    for (int i = 1; i < N; i++) 
        S[i] = S[i - 1] + phi[i]; 
} 
  
// Driver code 
int main() 
{ 
     int t;
    cin>>t;
    while(t--){
    // function call 
    CoPrimes(); 
   
    int a;
    cin>>a;
        cout << S[a] << endl; 
} 
}
