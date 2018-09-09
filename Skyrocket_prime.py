Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.

Example:

Input : n =10
Output : 2 3 5 7 

Input : n = 20 
Output: 2 3 5 7 11 13 17 19
The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is 
smaller than 10 million.

Here is the code in python:

s = set(range(2, 101))
while(l):
    p = min(s)
    print(p)
    s = s - set(range(p,101,p))


Time complexity:O(logn)

Its the most obstinate and efficient way to solve the puzzle of prime number which earlier was of O(n/2) complexity! 
