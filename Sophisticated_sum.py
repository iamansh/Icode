def ansh(a, b):
    while b!=0:
        data = a&b
        a=a^b
        b=data<<1
    return a
print(ansh(10, 6))    

It calculates the sum of any two numbers
