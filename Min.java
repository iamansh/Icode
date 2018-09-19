How to find minimum element in each row of 2 dimensional array;

 int A[][] = new int[100][100];   
  Scanner sc = new Scanner(System.in);
  int N=sc.nextInt();
  int M=sc.nextInt();
  int MIN[] = new int[M];  
  for(int i=0; i<N; i++){
     A[i][0]=sc.nextInt();
     MIN[i] = A[i][0];
     for(int j=1; j<M; j++){
      A[i][j]=sc.nextInt();
      if(MIN[i] > A[i][j])
         MIN[i] = A[i][j];
         }
      }
