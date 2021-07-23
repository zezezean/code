#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("magicin.txt","r",stdin);
    freopen("magicout.txt","w",stdout);
    int a,b,c;
    cin>>a>>b>>c;
    int t=max(b,c);
    int arr[3][3];
    arr[0][0]=a;arr[0][1]=b;arr[0][2]=19-a-b;arr[1][0]=c;arr[1][1]=18-t;arr[2][0]=19-a-c;
    int sum=a+b;
    arr[2][1]=19-b-arr[1][1];
    arr[1][2]=19-c-arr[1][1];
    arr[2][2]=19-arr[2][0]-arr[2][1];
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if (j!=2){cout<<arr[i][j]<<" ";}
            else{cout<<arr[i][j]<<endl;}
        }
    }
}