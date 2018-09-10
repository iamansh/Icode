                                                        DIGIT SUM

Given a digit and you need to print its super digit.
Super digit: All the digits of a particular number is being k times uptill it becomes a single digit. 

Ex: 123 3
    Number is to be mulitipiled with k.
    (1+2+3)+(1+2+3)+(1+2+3)=18 
    1+8=9
    Hence, 9 is the answer
    
    WHAT'S the logic in it?
    
    It has a trivial solution. 
    Just look at the super digits for the first one hundred natural numbers.
    Coupled with some divisibility rules / modular arithmetic, the answer is really simple, and doesn't use recursion.
    
    Special logic:
    
     The Digit Sum of a Number to Base 10 is Equivalent
     to Its Remainder Upon Division by 9.
     
     Python solution :
     m, k = map(int, input().split())
     x = n * k % 9
     print(x if x else 9)
     
     Java SOl:
     
     class A{
       public static void main(String[] x){
         Scanner sc = new Scanner(System.in);
         int m = sc.nextInt();
         int n = sc.nextInt();
         x = n * m % 9;
         System.out.println(x if x else 9);
         }
        } 
    
