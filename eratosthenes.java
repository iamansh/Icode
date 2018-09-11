                                                      SEIVE OF ERATOSTHENES
                                                     
import java.util.*;
class GFG{
  public static void main(String[] x){
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int k=0, i=0, j=0;
	int a[] = new int[n+1];
	int arr[] = new int[n+1];
	Arrays.fill(arr,1);
	for(i=1; i<=n; i++)
	   a[i] = sc.nextInt(); 
	
	for(k=1; k<=n; k++){ 
	   j = a[k];
	   for(i=j; i<=n; )
	      arr[i+=j] = 0; 
	 }

	System.out.println("primes are\n");
	for(i=1; i<=n; i++)
	   if(arr[i]==1)
	     System.out.println(arr[i]+" ");        
  }
}                                                      
