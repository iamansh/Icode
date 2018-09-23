One by one divide n by 2 until it becomes 0 and increment a count while doing this.
This count actually represents position of MSB.


def setBitNumber(n):
    if (n == 0):
        return 0
 
    msb = 0;
    while (n > 0):
        n = int(n / 2)
        msb += 1
 
    return (1 << msb)
n = 12
print(setBitNumber(n));
