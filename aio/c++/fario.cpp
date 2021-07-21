#include <bits/stdc++.h>
using namespace std;
using ll=long long;
#define endl "\n"

const int MAXN=1e5+5;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;cin>>n;int arr[n+1];
    for(int i=1;i<n+1;++i){cin>>arr[i];}
    int k;cin>>k; int index=1;
    while(k--){
        int b;cin>>b;
        while(arr[index]!=b){
            index++;
        }
        cout<<index<<endl;
    }
}