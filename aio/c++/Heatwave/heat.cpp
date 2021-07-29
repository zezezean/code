#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("heatin.txt","r",stdin);
    freopen("heatout.txt","w",stdout);
    int n, k, t, l=0, m=0;
    cin>>n>>k;
    for (int i=0;i<n;i++){
        cin>>t;
        if(t>=k){l++;}
        else{if(l>m){m=l;}l=0;}
    }
    m=max(l,m);
    cout<<m<<endl;
}