Suppose you have to take the following as input in python:

10 2 3 # n, u, k
3 1   #array of size u
5 2 8 #array of size k


What would you do...

n, u, k = map(int , input().strip().split())
for i in range(0, u):
   a=int(input())
   l.append(a)
for i in range(0, k):
   a=int(input())
   l1.appned(a)
   
   
   
   OLD FASHIONED! infact it will prompt out an error- 3 1 is treated as a two numbers(3 space 1)
   
   
   Sophisticated way! below
   
n, u, k = map(int, input().strip().split()) 
usb = sorted(map(int, input().strip().split()), reverse = True)
key = sorted(map(int, input().strip().split()))
   
   











