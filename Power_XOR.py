
“Given a set of numbers where all elements occur even number of times except one number, find the odd occurring number”  

I might suggest you to skim over the XOR:
XOR with the same number: returns 0
XOR with different breed: returns that breed

def ODD(l = [], n):
    r = 0
    for i in range(0, n):
      r ^= l[i]
    return r
    
l = [12, 12, 14, 90, 14, 14, 14]
n = sizeof(l)/sizeof(l[0])
print(ODD(l, n))
