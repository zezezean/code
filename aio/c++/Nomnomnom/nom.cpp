#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("nomin.txt","r",stdin);
    freopen("nomout.txt","w",stdout);
    int n,ans=0;
    scanf("%d",&n);
    int a[n+1];
    int cur,food;
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        if (i==0){food=a[i];cur=0;ans++;}
        else{
            cur+=a[i];
            if (cur>=food){
                food =cur;
                cur=0;
                ans++;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}