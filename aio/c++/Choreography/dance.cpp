#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("dancein.txt","r",stdin);
    freopen("danceout.txt","w",stdout);
    int d,t,ans=0;
    cin>>d>>t;
    int li[d+1]={0};
    for(int i = 0;i<t;i++){
        int a,b;
        cin>>a>>b;
        if (li[a]==0){
            ans++;
            li[a]=1;
        }
        li[a]--;
        li[b]++;
    }
    cout<<ans<<endl;
}