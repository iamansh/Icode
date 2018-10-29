Question:
Chef has a sequence of positive integers A1,A2,…,AN. He has only one question for you: is it possible to change at most K elements of this sequence to arbitrary positive integers in such a way that the condition
A21+A22+⋯+A2N≤A1+A2+⋯+AN
holds?

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing the string "YES" if it is possible to satisfy the given condition or "NO" otherwise.

Constraints
1≤T≤1,000
1≤K≤N≤104
1≤Ai≤10 for each valid i
the sum of N over all test cases does not exceed 105
Subtasks
Subtask #1 (100 points): original constraints

Example Input
1
2 2
1 2
Example Output
YES
Explanation
Example case 1: It is possible to change A2 to 1. This gives A=[1,1], for which the given condition holds, so the answer is "YES".


Solution:
import math
for i in range(int(input())):
    N, K = map(int, input().strip().split())
    if K>N:
        print("NO")
        continue
    A = list(sorted(map(int, input().strip().split())))
    B, sum1 = sum(A), 0
    
    for i in range(0, N):
        sum1 += int(math.pow(A[i], 2))
    if sum1 <= B:
        print("YES")
    else:
        sum1=0      
        for i in range(0, K):
               sum1+=1  #1 is the smallest positive integer
                #All elements upto k got changed to 1!
                
        for i in range(0, N-K):
            sum1 += int(math.pow(A[i], 2))
        if sum1 <= B:
            print("YES")
        else:                   
            print("NO")
   
