https://www.codechef.com/problems/HORSES


def solve(h):
    diff=h[1]-h[0]
    for i in range(1,len(h)-1):
        if h[i+1]-h[i]<diff:
            diff=h[i+1]-h[i]
    print(diff)

for t in range(int(input())):
    n=int(input())
    h=[int(x) for x in input().split()]
    solve(sorted(h))
