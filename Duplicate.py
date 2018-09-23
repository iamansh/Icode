   arr[] = {2, 4, 7, 9, 2, 4}
1) Get the XOR of all the elements.
     xor = 2^4^7^9^2^4 = 14 (1110)
2) Get a number which has only one set bit of the xor.   
   Since we can easily get the rightmost set bit, let us use it.
     set_bit_no = xor & ~(xor-1) = (1110) & ~(1101) = 0010
   Now set_bit_no will have only set as rightmost set bit of xor.
3) Now divide the elements in two sets and do xor of         
   elements in each set, and we get the non-repeating 
   elements 7 and 9. Please see implementation for this   
   step.





l = [2, 4, 7, 9, 2, 4]
a, b, x, set= 0, 0, 0, 0
for i in range(0, len(l)):
    x = x^l[i]
set = x & ~(x-1)
for i in range(0, len(l)):
    if l[i] & set:  
        a = a^l[i]
    else l[i] & set:
        b = b^l[i]        
print(a)
print(b)
