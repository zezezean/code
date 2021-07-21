#include <bits/stdc++.h>
using namespace std;

const int MAXN=1e6+1;

int arr[MAXN],ml,mr,n,ans;
bool lef[MAXN];
bool rig[MAXN];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    freopen("atlanin.txt","r",stdin);
    freopen("atlanout.txt","w",stdout);
    cin>>n;
    for(int i=0;i<n;++i){
        cin>>arr[i];
    }
    for(int i=0;i<n;++i){
        if(mr>arr[i]){rig[i]=true;}
        else mr=arr[i];
    }
    for(int i=n-1;i>=0;--i){
        if(ml>arr[i]){lef[i]=true;}
        else ml=arr[i];
    }
    for(int i=0;i<n;++i){
        if(lef[i]&&rig[i])ans++;
    }
    cout<<ans<<endl;
}