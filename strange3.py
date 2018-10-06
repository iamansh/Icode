Input value:

10 2 3
3 1
5 2 8


s, n, m = sorted(map(int, input().strip().split()))
keyboard = sorted(map(int, input().strip().split()), reverse=True)
usb = sorted(map(int, input().strip().split()))

o/p: 2 3 10
     [3, 1]
     [2, 5, 8]


                                    VS
                                    
                                    
                                    
s, n, m = sorted(map(int, input().strip().split()))
keyboard = list(sorted(map(int, input().strip().split()), reverse=True))
usb = list(sorted(map(int, input().strip().split())))                              


o/p: 2 3 10
     [3, 1]
     [2, 5, 8]
