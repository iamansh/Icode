                                                 HOW TO CALCULATE NUMBER OF ELEMETS in an array SKYROCKETLY!?
                                                 
Earilier the method was of counting the numbers explicitly, but now i hve come across with a new logic which is pretty obstinate!

The underneath method is offensive when an arrya has to be taken explicitly by an user.

int main(){
  int n;
  cin>>n;
  int a[n];
  for(int i=0; i<n; i++){
     cin>>a[i];
     c++;
     }
  cout<<"No. of elements"<<c;
  }
 
 But, what if an array is already given. How u then calculate the no. of elements?
 
 int main(){
 int arr[] = {5, 4, 3};
    int n = sizeof(arr)/sizeof(arr[0]);//elements
    }
