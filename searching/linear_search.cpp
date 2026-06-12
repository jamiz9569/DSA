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

    bool found = false;
    for(int i = 0 ; i < n ; i++){
        if(arr[i] == key){
            found = true;
            cout<<"Element found at index : "<<i<<endl;
            break;
        }
    }    if(!found){
        cout<<"Element not found in the array."<<endl;
    }
    return 0;
}