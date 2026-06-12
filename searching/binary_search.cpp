#include<iostream>
using namespace std;

int main() {
    // Your code here
    int n , key ;
    
    cout<<"Enter the size of the array : ";
    cin>>n;

    int arr[n];
    cout<<"Enter the elements of the array : ";
    for(int i = 0 ; i < n ; i++){
        cin>>arr[i];
    }

    cout<<"Enter the key to be searched : ";
    cin>>key;

    int low = 0;
    int high = n-1 ;
    //   int mid = (low + (high - low ))/2 ;
    bool found = false;

    while(low <= high){
      int mid = (low + (high - low ))/2 ;  // to avoid overflow 
      if (arr[mid] == key){
        found = true;
        cout <<" key has been found ";
      }
      else if ( key < arr[mid] ){
        high = mid -1 ;
      }
      else{
        low = mid +1;
      }
      
       if(!found){
       cout<<"Element not found in the array."<<endl;
       }
    }
    return 0;
}
