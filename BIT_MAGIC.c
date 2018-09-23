Count set bits in integer

Loop through all bits in an integer, check if a bit is set and if it is then increment the set bit count. See below program.

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
i = 9
print(countSetBits(i))
 
 
 
 
 
 
 
 Checking if given 32 bit integer is power of 2

int isPowerof2(int x)
{
    return (x && !(x & x-1));
}
Logic: All the power of 2 have only single bit set e.g. 16 (00010000). 
If we minus 1 from this, all the bits from LSB to set bit get toggled, i.e., 16-1 = 15 (00001111). 
Now if we AND x with (x-1) and the result is 0 then we can say that x is power of 2 otherwise not.
We have to take extra care when x = 0.

Example
x = 16(000100000)
x – 1 = 15(00001111)
x & (x-1) = 0
so 16 is power of 2

 
 

Lower to Upper Case
This method simply subtracts a value of 32 from the ASCII value of lowercase letter by 
Bitwise ANDing (&) with negation (~) of 32 converting the letter to uppercase.


#include<stdio.h>
 
const int x = 32;
 
char *toUpperCase(char *a)
{
    for (int i=0; a[i]!='\0'; i++)
        a[i] = a[i] & ~x;
 
    return a;
}
 
int main()
{
    char str[] = "anshsrivastava";
    printf("%s", toUpperCase(str));
 
    return 0;
}







Upper to Lower Case
Similarly, it adds a value of 32 to the ASCII value of uppercase letter by Bitwise ORing (|) with 32 converting the letter to lowercase.


#include<stdio.h>
const int x = 32;
 

char * toLowerCase(char *a)
{
    for (int i=0; a[i]!='\0'; i++)
        a[i] = a[i] | x;
 
    return a;
}
 
int main()
{
    char str[] = "SanjaYKannA";
    printf("%s", toLowerCase(str));
    return 0;
}
